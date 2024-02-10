# serializers.py
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'regno', 'kmail', 'club', 'permission', 'contact_number', 'joined_date', 'left_date', 'hostel', 'password','name']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = KH_Project
        fields = '__all__'


class PunchTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KIDS_PunchTime
        fields = '__all__'


class ListPunchTimeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = KIDS_PunchTime
        fields = '__all__'

class ListProjectSerializer(serializers.ModelSerializer):
    team_leader = UserSerializer()
    members = UserSerializer(many=True)

    class Meta:
        model = KH_Project
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KH_Club_Members_Attendanance
        fields = '__all__'


class ListAttendanceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    project = ProjectSerializer()

    class Meta:
        model = KH_Club_Members_Attendanance
        fields = '__all__'

class Create_KH_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = KIDS_Permission
        fields = '__all__'

class KH_PermissionSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
        model = KIDS_Permission
        fields = '__all__'