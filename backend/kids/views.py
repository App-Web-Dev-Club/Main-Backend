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



User = get_user_model()


class Test(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
        

class ProjectListCreateAPIView(APIView):
    permission_classes = [AllowAny]
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
    permission_classes = [AllowAny]

    def get_user_object(self, reg):
        try:
            test =  Student.objects.get(register_no=reg)
            return test
        except Student.DoesNotExist:
            return None
        
    def get(self, request, *args, **kwargs):
        attendance_entries = KH_Club_Members_Attendanance.objects.all()
        serializer = ListAttendanceSerializer(attendance_entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.user.permission == 'CLUB_LEADER':
            regno = request.data.get('register_no')
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


class Studentid(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        reg = request.data.get('register_no')
        student = Student.objects.filter(register_no = reg).first()
        if student:
            serializer = StudentSerializer(student)
            print(serializer.data)
            return Response(serializer.data)
        return Response('User not found or invalid')


class project_under_user(APIView):
    permission_classes = [AllowAny]

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
        return Response(res)

class PermissionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        data = KIDS_Permission.objects.all()
        serializer = KHPermissionSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = Create_KH_PermissionSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()

            data = KIDS_Permission.objects.filter(id = instance.id)
            serializer = KHPermissionSerializer(data, many=True)
            return Response(serializer.data)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FaceAttendanceListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get_user_object(self, reg):
        try:
            test =  User.objects.get(regno=reg)
            return test
        except User.DoesNotExist:
            return None
        
    def get(self, request, *args, **kwargs):
        attendance_entries = KH_Club_Members_Attendanance.objects.all()
        serializer = ListAttendanceSerializer(attendance_entries, many=True)
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
    permission_classes = [AllowAny]

    def get_user_object(self, reg):
        try:
            test =  User.objects.get(regno=reg)
            # print(test)
            return test
        except User.DoesNotExist:
            return None
        
    def get(self, request, *args, **kwargs):
        attendance_entries = KIDS_PunchTime.objects.all()
        serializer = ListPunchTimeSerializer(attendance_entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
            regno = request.data.get('regno')
            paticipant = self.get_user_object(regno)

            if paticipant is None:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            data = {
                'user':paticipant.id,
            }

            serializer = PunchTimeSerializer(data=data)
            if serializer.is_valid():
                # Assign the user object to the Attendance instance before saving
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    

class PunchTimeGETView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        type = request.data.get('type')


        if type == 'Day':
            twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
            punch_times = KIDS_PunchTime.objects.filter(time__gte=twenty_four_hours_ago)
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
            user_regno = request.data.get('regno')
            punch_times = KIDS_PunchTime.objects.filter(user__regno=user_regno)
            serializer = ListPunchTimeSerializer(punch_times, many=True)
            # sorted_data = sorted(serializer.data, key=lambda x: x['user']['regno'])
            return Response(serializer.data, status=status.HTTP_200_OK)
 
        else:
            return Response({'error': 'Invalid type specified'}, status=status.HTTP_400_BAD_REQUEST)
            


from django.core.mail import send_mail

class SendEmailView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.data.get('subject', '')
        message = request.data.get('message', '')
        from_email = 'biwinfelix@example.com'
        recipient_list = [request.data.get('to_email', '')]


        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return Response({'detail': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': f'Failed to send email. Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
