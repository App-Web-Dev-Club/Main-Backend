from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from inventory.models import *
from kids.models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


from inventory.serializers import *
# Create your views here.


class ProductAPIView(APIView):

    def get(self, request):
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductRequestAPIView(APIView):

    def get(self, request):
        data = ProductRequest.objects.all()
        serializer = ProductRequestSerializer(data, many=True)
        return Response(serializer.data)
  
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductManagementAPIView(APIView):

    def get(self, request):
        data = ProductManagment.objects.all()
        serializer = ProductMangementSerializer(data, many=True)
        return Response(serializer.data)
  
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductMangementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminLogin(APIView):
    def post(self,request):
        email = request.data.get('email') 
        password = request.data.get('password')

        user = User.objects.filter(email=email, role='administrator').first()
        flt = Faculty.objects.filter(user= user).first()

        if user is not None and authenticate(email=email, password = password):
            if flt:
                custom_data = {
                'faculty id': flt.faculty_id,
                'email':user.email,
                'role': user.role,
                # 'club': mem.club,
                # 'permission': mem.permission,
                }
                refresh = RefreshToken.for_user(user)
                refresh.access_token.payload.update(custom_data)
                response_data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'email': user.email,
                    'role': user.role,
                    # 'club': mem.club,
                    # 'permission': mem.permission, 
                }
                return Response(response_data)
            else:
                return Response('You are Not a Faculty')
            
        else:
            return Response('nope')

