from api.models import *
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class KH_Club_Members(AbstractUser):
    regno = models.CharField(max_length=120, unique=True)
    permission_choices = [
        ('ADMIN', 'Admin'),
        ('CLUB_LEADER', 'ClubLeader'),
        ('MEMBER','Member'),
    ]
    club_choices =[
        ('3D','3d'),
        ('AI','Ai'),
        ('WEB_AND_APP','Web_And_App'),
        ('IOT_AND_ROBOTICS','Iot_And_Robotics'),
        ('XOR','Xor'),
        ('CYBERSECURITY','Cybersecurity'),
        ('COMPETITIVE_PROGRAMMING','Competitive_Programming'),
    ]
    kmail = models.EmailField(default=None)
    club = models.CharField(max_length=100,choices = club_choices)
    permission = models.CharField(max_length=100,choices = permission_choices)
    contact_number = models.CharField(max_length=15,default=None)
    joined_date = models.DateField(default=None)
    left_date = models.DateField(null=True, blank=True)
    hostel = models.CharField(max_length=255, default=None)
    name = models.CharField(max_length= 200,null=True,default = True)
    
    username = ""
    USERNAME_FIELD='regno'

    REQUIRED_FIELDS =['kmail']




class KH_Project(models.Model):
    project_title = models.CharField(max_length=255)
    project_description = models.TextField()
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_leader_projects')
    members = models.ManyToManyField(User, related_name='member_projects')
    started_date = models.DateField(auto_now_add = True)
    completion_date = models.DateField(null=True, blank=True)

    status_choices = [
        ('progress', 'Progress'),
        ('completed', 'Completed'),
        ('onhold', 'Onhold'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='IN_PROGRESS')


    def __str__(self):
        return self.project_title
class KH_Club_Members_Attendanance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(KH_Project, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)
    work_done = models.TextField()


    def __str__(self):
        return f"{self.User.User.Username} - {self.project.project_title} - {self.date}"
    

class KIDS_Permission(models.Model):
    user = models.ManyToManyField(User)
    date_time = models.DateTimeField(auto_now_add=True)
    CHOICES = [
        ('Late Permission', 'Late_Permission'),
        ('Night Stay Permission', 'Night_Stay_Permission'),
    ]
    type = models.CharField(max_length=100, choices=CHOICES)


class KIDS_PunchTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add= True)


