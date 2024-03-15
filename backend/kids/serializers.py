from rest_framework import serializers
from api.models import *
from .models import *
from api.serializers import *

class ListKHClubMembersSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = KH_Club_Members
        fields = '__all__'
        depth=2

class KHClubMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = KH_Club_Members
        fields = '__all__'


class KHProjectListSerializer(serializers.ModelSerializer):
    project_lead = KHClubMembersSerializer()  
    kh_members = KHClubMembersSerializer(many = True)  

    class Meta:
        model = KH_Project
        fields = '__all__'


class ListKHClubMembersAttendananceSerializer(serializers.ModelSerializer):
    # user = KHClubMembersSerializer()
    
    class Meta:
        model = KH_Club_Members_Attendanance
        fields = '__all__'
        depth = 3

class KHClubMembersAttendananceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    project = KHProjectListSerializer()
    class Meta:
        model = KH_Club_Members_Attendanance
        fields = '__all__'

class KHPermissionSerializer(serializers.ModelSerializer):
    user = StudentSerializer(many=True)
    class Meta:
        model = KIDS_Permission
        fields = '__all__'



class Create_KH_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = KIDS_Permission
        fields = '__all__'       


class ListPunchTimeSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    regno = StudentSerializer()
    # regno_ = StudentSerializer()

    class Meta:
        model = KIDS_PunchTime
        fields = '__all__'


class PunchTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KIDS_PunchTime
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = KH_Project
        fields = '__all__'

class ListProjectSerializer(serializers.ModelSerializer):
    # project_lead = KHClubMembersSerializer()
    # kh_members = KHClubMembersSerializer(many=True)

    class Meta:
        model = KH_Project
        fields = '__all__'
        depth = 3

class CreateAttendanceSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # project = ProjectSerializer()

    class Meta:
        model = KH_Club_Members_Attendanance
        fields = '__all__'

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'

# class HackathonParticipantsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = HackathonParticipants
#         fields = '__all__'



