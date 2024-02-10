from .models import User
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .permissions import *
from django.core.mail import send_mail


class TestView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
            subject = 'Happy Birthday!'
            message = f"Dear,\n\nHappy Birthday!\n\nBest wishes from us!"
            from_email = 'biwinfelix@gmail.com'  # Update with your email
            to_email = ['bewinfelix25@gmail.com']

            send_mail(subject, message, from_email, to_email)
            return Response('sucess')
    
    
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(ObtainAuthToken):
    permission_classes=[AllowAny]
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password = password)
        data = User.objects.filter(email=email, role='guest').first()
        if user is not None  and data is not None:
            refresh = RefreshToken.for_user(user)
            custom_data = {
                'email':data.email,
                'role': 'guest',
            }
            refresh['custom_data'] = custom_data
            refresh.access_token.payload['custom_data'] = custom_data

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'email': data.email,
                'role': 'guest',
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']  # Assuming refresh token is sent in request body
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logged out successfully'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)   

class StudentRegistrationView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacultyRegistrationView(APIView):
    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class StudentLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email') 
        password = request.data.get('password')
        user = User.objects.filter(email=email, role='student').first()
        
        if user is not None and authenticate(email=email, password = password):
            refresh = RefreshToken.for_user(user)
            student = user.student
            student_data = StudentSerializer(student).data

            custom_data = {
                'register_no': student.register_no,
                'email':user.email,
                'role': user.role,
            }
            refresh['custom_data'] = custom_data
            refresh.access_token.payload['custom_data'] = custom_data

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'email': user.email,
                'role': user.role,
                'student':student.register_no
            }

            return Response(response_data, status=status.HTTP_200_OK)
        elif User.objects.filter(email=email):
            return Response({'message': 'You are not a student'}, status=status.HTTP_401_UNAUTHORIZED)
        
        else:
            return Response({'message': 'Invalid User'}, status=status.HTTP_401_UNAUTHORIZED)

class FacultyLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email') 
        password = request.data.get('password')

        user = User.objects.filter(email=email, role='faculty').first()
        if user is not None and authenticate(email=email, password = password):
            refresh = RefreshToken.for_user(user)
            faculty = user.faculty
            
            custom_data = {
                'faculty_id': faculty.faculty_id,
                'email':user.email,
                'role': user.role,
            }
            refresh['custom_data'] = custom_data
            refresh.access_token.payload['custom_data'] = custom_data

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'email': user.email,
                'role': user.role,
                'faculty_id': faculty.faculty_id,
            }

            if user.role == 'teacher':
                faculty = user.faculty 
                if faculty is not None:
                    faculty_data = FacultySerializer(faculty).data
                    response_data['data'] = faculty_data

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid email or authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)





    

# from django.contrib.auth import authenticate

# class RegisterView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

# class LoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         username = request.data.get('register_no')
#         password = request.data.get('password')
#         if not username or not password:
#             return Response({'error': 'Please provide both username and password'}, 
#                             status=status.HTTP_400_BAD_REQUEST)
#         user = authenticate(request, username=username, password=password)
#         if not user:
#             return Response({'error': 'Invalid Credentials'}, 
#                             status=status.HTTP_401_UNAUTHORIZED)
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })


# class RefreshTokenView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         refresh_token = request.data.get('refresh')

#         if not refresh_token:
#             return Response({'error': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             refresh = RefreshToken(refresh_token)
#             access_token = str(refresh.access_token)
#             return Response({'access_token': access_token}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)   




    









