from django.db import models
from api.models import *
# Create your models here.

class KH_Club_Members(models.Model):
    regno = models.OneToOneField(Student, on_delete = models.CASCADE, related_name='club_member')
    club_choices =[
        ('3D','3d'),
        ('AI','Ai'),
        ('WEB_AND_APP','Web_And_App'),
        ('IOT_AND_ROBOTICS','Iot_And_Robotics'),
        ('XOR','Xor'),
        ('CYBERSECURITY','Cybersecurity'),
        ('COMPETITIVE_PROGRAMMING','Competitive_Programming'),
    ]

    club = models.CharField(max_length=100,choices = club_choices)
    permission_choices = [
        ('ADMIN', 'Admin'),
        ('CLUB_LEADER', 'ClubLeader'),
        ('MEMBER','Member'),
    ]
    permission = models.CharField(max_length=100,choices = permission_choices)
    join_date = models.DateTimeField(auto_now_add= True)
    edited_date = models.DateTimeField(auto_now=True)
    left_date = models.DateField(null=True, blank=True)


class KH_Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project_lead = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE, related_name='project_led')
    kh_members = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE, related_name='project_team')

    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('onprocess', 'On Process'),
        ('completed', 'Completed'),
        ('hold', 'Hold'),
    ]
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)

class KH_Club_Members_Attendanance(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    word_done = models.TextField()
    project = models.ForeignKey(KH_Project, on_delete = models.CASCADE)
    user = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE, related_name='club_attendances')


class KIDS_Permission(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='permissions')
    date_time = models.DateTimeField()
    CHOICES = [
        ('late_night', 'Late_Night'),
        ('1st_year', '1st_Year'),
        ('holiday ', 'Holiday '),
    ]
    type = models.CharField(max_length=100, choices=CHOICES)


class KIDS_PunchTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add= True)
