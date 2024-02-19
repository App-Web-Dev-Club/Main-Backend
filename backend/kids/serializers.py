from rest_framework import serializers
from api.models import *
from .models import *
from api.serializers import *

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


class KHClubMembersAttendananceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    project = KHProjectListSerializer()
    class Meta:
        model = KH_Club_Members_Attendanance
        fields = '__all__'

class KHPermissionSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
        model = KIDS_Permission
        fields = '__all__'



class Create_KH_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = KIDS_Permission
        fields = '__all__'       


class ListPunchTimeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
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
    team_leader = UserSerializer()
    members = UserSerializer(many=True)

    class Meta:
        model = KH_Project
        fields = '__all__'

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

class HackathonParticipantsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HackathonParticipants
        fields = '__all__'



