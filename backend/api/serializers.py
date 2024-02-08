from rest_framework import serializers
from .models import *



class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role', 'gender','dob','contact_number']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # print(user)
        return user


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'user', 'register_no', 'branch', 'dept', 'year_of_joining', 'year_of_studys', 'passout_year','hostel', 'student_status']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student





class FacultySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Faculty
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        student = Faculty.objects.create(user=user, **validated_data)
        return student




# class Attendanance_typeSerializer(serializers.ModelSerializer):
#     class Meta:
#         models = Attendanance_type
#         fields = '__all__'


# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = '__all__'

# class EventListSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField()
#     type_of_attendance = serializers.StringRelatedField()
#     paticipants = serializers.StringRelatedField()
#     attendanance_markers = serializers.StringRelatedField()

#     class Meta:
#         model = Event
#         exclude = ('user', 'paticipants', 'attendanance_markers')



# class AttendananceTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendanance_type
#         fields = '__all__'

# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = '__all__'

# class EventAttendananceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event_Attendanance
#         fields = '__all__'

# class KHClubMembersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KH_Club_Members
#         fields = '__all__'

# class KHProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KH_Project
#         fields = '__all__'

# class KHClubMembersAttendananceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KH_Club_Members_Attendanance
#         fields = '__all__'

# class KHPermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KH_Permission
#         fields = '__all__'








# class EventListSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     type_of_attendance = AttendananceTypeSerializer()  
#     paticipants = UserSerializer()
#     attendanance_markers = UserSerializer()

#     class Meta:
#         model = Event
#         fields = '__all__'

# class KHClubMembersAttendananceListSerializer(serializers.ModelSerializer):
#     project = KHProjectSerializer()   
#     user = KHClubMembersSerializer()  

#     class Meta:
#         model = KH_Club_Members_Attendanance
#         fields = '__all__'

# class KHProjectListSerializer(serializers.ModelSerializer):
#     project_lead = KHClubMembersSerializer()  
#     kh_members = KHClubMembersSerializer()  

#     class Meta:
#         model = KH_Project
#         fields = '__all__'



