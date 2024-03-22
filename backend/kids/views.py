from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import *
from .models import *
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .pdfgenerator import *
from django.urls import reverse
import requests




User = get_user_model()


class KH_Login(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        email = request.data.get('email') 
        password = request.data.get('password')
        
        user = User.objects.filter(email=email, role='student').first()
        stu = Student.objects.filter(user= user).first()
        mem = KH_Club_Members.objects.filter(regno= stu).first()
        # return Response('You are Not a user')
        if user is not None and authenticate(email=email, password = password):
            if mem:
                custom_data = {
                'register_no': stu.register_no,
                'email':user.email,
                'role': user.role,
                'club': mem.club,
                'permission': mem.permission,
                }
                refresh = RefreshToken.for_user(user)
                refresh.access_token.payload.update(custom_data)
                response_data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'email': user.email,
                    'role': user.role,
                    'club': mem.club,
                    'permission': mem.permission, 
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response('You are Not a Member', status=status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response('You are Not a user')



class Test(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
        

class ProjectListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        projects = KH_Project.objects.all()
        serializer = KHProjectListSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceListCreateAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]

    def get_user_object(self, reg):
        try:
            test =  Student.objects.filter(register_no=reg).first()
            mem = KH_Club_Members.objects.filter(regno = test).first()
            # print(mem)
            return mem
        except Student.DoesNotExist:
            print('tt')
            return None
        
    def get(self, request, *args, **kwargs):
        attendance_entries = KH_Club_Members_Attendanance.objects.all()
        serializer = KHClubMembersAttendananceSerializer(attendance_entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # stu = Student.objects.filter(user= request.user.id).first()
        # mem = KH_Club_Members.objects.filter(regno= stu).first()
    

        if True:
            regno = request.data.get('register_no')
            paticipant = self.get_user_object(regno)
            # print(paticipant)

            if paticipant is None:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            data = {
                'user':paticipant.id,
                'project':request.data.get('project'),
                'work_done':request.data.get('work_done') or "dwadwadaw"
            }
            print(data)
            serializer = CreateAttendanceSerializer(data=data)
            if serializer.is_valid():
                # Assign the user object to the Attendance instance before saving
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
        return Response('User permission required contact administator')


class Studentid(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        reg = request.data.get('register_no')
        student = Student.objects.filter(register_no = reg).first()
        if student:
            serializer = StudentSerializer(student)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('User not found or invalid')
    
class Memberid(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        reg = request.data.get('register_no')
        student = Student.objects.filter(register_no = reg).first()
        test = KH_Club_Members.objects.filter(regno = student).first()

        if test:
            serializer = ListKHClubMembersSerializer(test)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('User not found or invalid')


class project_under_user(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_object(self, reg):
        try:
            test =  Student.objects.filter(register_no=reg).first()
            serializer = StudentSerializer(test)
            return serializer.data['id']
        except Student.DoesNotExist:
            return None

    def post(self,request, *args, **kwargs):
        reg = request.data.get('register_no')
        userid = self.get_user_object(reg)

        projects_member = KH_Project.objects.filter(kh_members =userid )
        projects_lead = KH_Project.objects.filter(project_lead =userid )

        serializer_member = ProjectSerializer(projects_member,many = True)
        serializer_lead = ProjectSerializer(projects_lead,many = True)

        res = {
            'userid': userid,
            'member' : serializer_member.data,
            'lead':serializer_lead.data
        }
        return Response(res, status=status.HTTP_201_CREATED)
    

class project_under_member(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_object(self, reg):
        try:
            test =  Student.objects.filter(register_no=reg).first()
            test2 = KH_Club_Members.objects.filter(regno = test).first()
            serializer = ListKHClubMembersSerializer(test2)
            print(serializer.data)
            return serializer.data['id']
        except Student.DoesNotExist:
            return None

    def post(self,request, *args, **kwargs):
        reg = request.data.get('register_no')
        userid = self.get_user_object(reg)

        projects_member = KH_Project.objects.filter(kh_members =userid )
        projects_lead = KH_Project.objects.filter(project_lead =userid )

        serializer_member = ProjectSerializer(projects_member,many = True)
        serializer_lead = ProjectSerializer(projects_lead,many = True)

        res = {
            'userid': userid,
            'member' : serializer_member.data,
            'lead':serializer_lead.data
        }
        return Response(res, status=status.HTTP_201_CREATED)

from datetime import datetime, timedelta

from django.core.mail import EmailMessage
class PermissionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = KIDS_Permission.objects.all()
        serializer = KHPermissionSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        form_type = request.data.get("form_type")
        # twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
        # punch_times = KIDS_PunchTime.objects.filter(time__gte=twenty_four_hours_ago)
        # serializer = ListPunchTimeSerializer(punch_times, many=True)

        today_date = datetime.now().date()
        # start_of_day_430pm = datetime.combine(today_date, datetime.min.time()) + timedelta(hours=16, minutes=30)

        # Set the time to 5:00 PM for today's date
        start_of_day_5pm = datetime.combine(today_date, datetime.min.time()) + timedelta(hours=17)
        print(start_of_day_5pm)

        
        # Set the time to 12:00 AM for today's date
        start_of_day = datetime.combine(today_date, datetime.min.time())
        # print(start_of_day)
        # Get the punch times within today's date starting from 12:00 AM
        punch_times = KIDS_PunchTime.objects.filter(time__gte=start_of_day)
        serializer = ListPunchTimeSerializer(punch_times, many=True)

        print(serializer.data)

        main_data = {
            'type':form_type,
            'user': serializer.data,
            
        }

        # code for, Form code -------------------------------------------

        first_code = FormCode.objects.all()
        first_code_serializer = FormCodeSerializer(first_code, many=True)

        code = first_code_serializer.data[-1]['code']+1
        # print(code)

        code_data = {
            'code':code
        }
        
        second_code_serializer = FormCodeSerializer(data=code_data)
        if second_code_serializer.is_valid():
            second_code_serializer.save()
            print(second_code_serializer.data['code'])
        else:
            print("oh shit")

        code_pdf = second_code_serializer.data['code']
        # end of the code --------------------------------------------------

        if form_type == "Late Permission":
            pdf_buffer = generate_permission_pdf(serializer.data,code_pdf)  # Assuming this function returns the PDF buffer
            subject = "Late Permission Form"
        else:
            pdf_buffer = generate_night_permission_pdf(serializer.data,code_pdf)
            subject = "Night Permission Form"
        
        message = "This is a generated message"
        from_email = 'J2r1N.04@gmail.com'
        recipient_list = ["chijithjerin@karunya.edu.in"]

        email = EmailMessage(subject, message, from_email, recipient_list)
        email.attach('permission.pdf', pdf_buffer.getvalue(), 'application/pdf')


        try:
            
            email.send()
            return Response({'detail': 'Email sent successfully','user': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': f'Failed to send email. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



        # response = requests.post(url, data=payload)
        # # print(response)
        # # serializer = Create_KH_PermissionSerializer(data=request.data)
        # # data = KIDS_Permission.objects.filter(id = instance.id)
        # # serializer = KHPermissionSerializer(data, many=True)
        # # return Response(serializer.data)
        
        # if response.status_code == 500:
        #     # Email sent successfully
        #     print("hello")
        #     return Response(main_data, status=status.HTTP_201_CREATED)
        # else:
        #     # Failed to send email
            
        #     return Response({'detail': 'Failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FaceAttendanceListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_object(self, reg):
        try:
            test =  User.objects.get(regno=reg)
            return test
        except User.DoesNotExist:
            return None
        
    def get(self, request, *args, **kwargs):
        attendance_entries = KH_Club_Members_Attendanance.objects.all()
        serializer = KHClubMembersAttendananceSerializer(attendance_entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.user.permission == 'CLUB_LEADER':
            regno = request.data.get('regno')
            paticipant = self.get_user_object(regno)

            if paticipant is None:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            data = {
                'user':paticipant.id,
                'project':request.data.get('project'),
                'work_done':request.data.get('work_done')
            }
            serializer = KHClubMembersAttendananceSerializer(data=data)
            if serializer.is_valid():
                # Assign the user object to the Attendance instance before saving
                serializer.save(user=paticipant)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
        return Response('User permission required contact administator')
    

class PunchTimeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_object(self, reg):
        try:
            test =  Student.objects.filter(register_no=reg).first()
            serializer = StudentSerializer(test)
            name = serializer.data.get('user').get('name')
            # print(name)
            return test,name
        except Student.DoesNotExist:
            return None
        
    # def get_regno_objects(self,email):
    #     try:
    #         test = User.objects.filter(email=email)
    #         return test
    #     except User.DoesNotExist:
    #         return None
        
    def get(self, request, *args, **kwargs):
        attendance_entries = KIDS_PunchTime.objects.all()
        serializer = ListPunchTimeSerializer(attendance_entries, many=True)
        return Response(serializer.data)




    def post(self, request, *args, **kwargs):
            regno = request.data.get('regno')
            paticipant,name = self.get_user_object(regno)
            print(name)
            if paticipant is None:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
            # data = {
            #     'user':paticipant.id,
            # }

            data = {
                'name':name,
                'regno':paticipant.id,
            }
            serializer = PunchTimeSerializer(data=data)
            if serializer.is_valid():
                # Assign the user object to the Attendance instance before saving
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    

class PunchTimeGETView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        type = request.data.get('type')


        if type == 'Day':
            # twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
            # punch_times = KIDS_PunchTime.objects.filter(time__gte=twenty_four_hours_ago)
            # serializer = ListPunchTimeSerializer(punch_times, many=True)
            today_date = datetime.now().date()

            # Set the time to 12:00 AM for today's date
            start_of_day = datetime.combine(today_date, datetime.min.time())
            print(start_of_day)
            # Get the punch times within today's date starting from 12:00 AM
            punch_times = KIDS_PunchTime.objects.filter(time__gte=start_of_day)
            serializer = ListPunchTimeSerializer(punch_times, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif type == 'Month':
            # Assuming a month is defined as 30 days
            thirty_days_ago = datetime.now() - timedelta(days=30)
            punch_times = KIDS_PunchTime.objects.filter(time__gte=thirty_days_ago)
            serializer = ListPunchTimeSerializer(punch_times, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif type == 'Year':
            # Assuming a year is defined as 365 days
            one_year_ago = datetime.now() - timedelta(days=365)
            punch_times = KIDS_PunchTime.objects.filter(time__gte=one_year_ago)
            serializer = ListPunchTimeSerializer(punch_times, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif type == 'Week':
            # Assuming a week is defined as 7 days
            seven_days_ago = datetime.now() - timedelta(days=7)
            punch_times = KIDS_PunchTime.objects.filter(time__gte=seven_days_ago)
            serializer = ListPunchTimeSerializer(punch_times, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif type == 'User':
            user_regno = request.data.get('register_no')
            
            user = Student.objects.filter(register_no=user_regno).first()

            # usrid = user.id+1
            punch_times = KIDS_PunchTime.objects.filter(regno=user)
            # print(punch_times)
            serializer = ListPunchTimeSerializer(punch_times, many=True)
            # sorted_data = sorted(serializer.data, key=lambda x: x['user']['regno'])
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
 
        else:
            return Response({'error': 'Invalid type specified'}, status=status.HTTP_400_BAD_REQUEST)
            


from django.core.mail import send_mail


class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject', '')
        message = request.data.get('message', '')
        from_email = 'J2r1N.04@gmail.com'
        to_email = request.data.get('to_email', '')  # Assuming to_email is a string

        # pdf_buffer = generate_permission_pdf()

        try:
            email = EmailMessage(subject, message, from_email, [to_email])
            # email.attach('permission.pdf', pdf_buffer.getvalue(), 'application/pdf')
            email.send()

            return Response({'detail': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': f'Failed to send email. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HackathonAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,  *args, **kwargs):
        data = Hackathon.objects.all()
        serializer = HackathonSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request,  *args, **kwargs):
        data = request.data
        serializer = HackathonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ClubsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ListKHClubMembersSerializer
    queryset = KH_Club_Members.objects.all()

    def list(self, request, *args, **kwargs):
        search = request.GET.get("search")
        print("Search parameter:", search)
        queryset = self.queryset
            
        if search:
            queryset = queryset.filter(club__icontains=search)

        serializer = ListKHClubMembersSerializer(queryset, many=True)
        return Response(serializer.data)
    


class ListAttendanceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ListKHClubMembersAttendananceSerializer
    queryset = KH_Club_Members_Attendanance.objects.all()

    def list(self, request, *args, **kwargs):
        search = request.GET.get("search")
        filter_data = request.GET.get("filter")
        print("Search parameter:", search)
        queryset = self.queryset
            
        if search:
            queryset = queryset.filter(user__club__icontains=search)

        if filter_data:
            queryset = queryset.filter(user__regno__register_no__exact=filter_data)

        serializer = ListKHClubMembersAttendananceSerializer(queryset, many=True)
        return Response(serializer.data)




class ListProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ListProjectSerializer
    queryset = KH_Project.objects.all()


    def list(self, request, *args, **kwargs):
        search = request.GET.get("search")
        print("Search parameter:", search)
        queryset = self.queryset
            
        if search:
            queryset = queryset.filter(project_lead__club__icontains=search)

        serializer = ListProjectSerializer(queryset, many=True)
        return Response(serializer.data)
    






# class HackathonParticipantsAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request,  *args, **kwargs):
#         data = HackathonParticipants.objects.all()
#         serializer = HackathonParticipantsSerializer(data, many=True)
#         return Response(serializer.data)
    
#     def post(self, reqest,*args, **kwargs):
#         data = reqest.data 
#         serializer = HackathonParticipantsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)