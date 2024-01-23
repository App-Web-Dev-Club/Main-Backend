from .models import User
from .serializers import *
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        user = authenticate(request, email=email)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
            return Response({'token': token.key, 'username': user.username, 'role': user.role})
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
        user = User.objects.filter(email=email, role='student').first()

        if user is not None:
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'email': user.email,
                'role': user.role,
            }

            if user.role == 'student':
                student = user.student  # Assuming the related name is "student"
                if student is not None:
                    # Add student data to the response data
                    student_data = StudentSerializer(student).data
                    response_data['data'] = student_data

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid email or authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)





class FacultyLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email') 
        user = User.objects.filter(email=email, role='teacher').first()

        if user is not None:
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'email': user.email,
                'role': user.role,
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



class TestView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serialized_user = TestSerializer(users, many=True)
        return Response(serialized_user.data)
    

















