from rest_framework import serializers
from .models import *



# class TestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True}}  # Password should only be written, not displayed

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance


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



class AttendananceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendanance_type
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventAttendananceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Attendanance
        fields = '__all__'

class KHClubMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = KH_Club_Members
        fields = '__all__'

class KHProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = KH_Project
        fields = '__all__'

class KHClubMembersAttendananceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KH_Club_Members_Attendanance
        fields = '__all__'

class KHPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = KH_Permission
        fields = '__all__'








class EventListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    type_of_attendance = AttendananceTypeSerializer()  
    paticipants = UserSerializer()
    attendanance_markers = UserSerializer()

    class Meta:
        model = Event
        fields = '__all__'

class KHClubMembersAttendananceListSerializer(serializers.ModelSerializer):
    project = KHProjectSerializer()   
    user = KHClubMembersSerializer()  

    class Meta:
        model = KH_Club_Members_Attendanance
        fields = '__all__'

class KHProjectListSerializer(serializers.ModelSerializer):
    project_lead = KHClubMembersSerializer()  
    kh_members = KHClubMembersSerializer()  

    class Meta:
        model = KH_Project
        fields = '__all__'
