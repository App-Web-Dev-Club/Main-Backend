from django.db import models
from api.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class KH_Club_Members(models.Model):
    regno = models.OneToOneField(Student, on_delete = models.CASCADE, related_name='club_member')
    club_choices =[
        ('3D','3d'),
        ('AI','Ai'),
        ('WEB AND APP','Web_And_App'),
        ('IOT AND ROBOTICS','Iot_And_Robotics'),
        ('XOR','Xor'),
        ('CYBER SECURITY','Cyber security'),
        ('COMPETITIVE PROGRAMMING','Competitive Programming'),
        ('BUILD CLUB','Build club'),
        ('GDSC','Google Developers Student Club'),
        ('Neural network','Neural network '),
        ('KH Core','Khacks Core Team'),

        ('Ecell core','Ecell Core'),
        ('Accelerator club','Accelerator club'),
        ('Women Entrepreneur Club','Women Entrepreneur Club'),
        ('Resource hub','resource hub'),
        ('Start up','start up'),

        ('Kreatives core','kreatives core'),
        ('TEDX','TEDX'),
        ('Design club','Design club'),
        ('Writters club','Writters club'),

        ('KIDS','KIDS')
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
    kh_members = models.ManyToManyField(KH_Club_Members)

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
    work_done = models.TextField()
    project = models.ForeignKey(KH_Project, on_delete = models.CASCADE)
    user = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE, related_name='club_attendances')


class KIDS_Permission(models.Model):
    user = models.ManyToManyField(Student)
    date_time = models.DateTimeField()
    CHOICES = [
        ('late_night', 'Late_Night'),
        ('1st_year', '1st_Year'),
        ('holiday ', 'Holiday '),
    ]
    type = models.CharField(max_length=100, choices=CHOICES)


class KIDS_PunchTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    regno = models.ForeignKey(Student, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add= True)


class Hackathon(models.Model):
    name = models.CharField(max_length=255)
    shot_description = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    conducting_organization = models.CharField(max_length=255)
    registation_date = models.DateTimeField()
    website_link = models.URLField()
    registation_link = models.URLField()
    whatsapplink = models.URLField()
    gcr_code = models.CharField(max_length=255)
    end_Date = models.DateTimeField()
    banner = models.ImageField(upload_to='hacakthon/banner/')
    create_date = models.DateTimeField(auto_now_add= True)
    active = models.BooleanField(null=True,default = True,blank=True)

@receiver(post_save, sender=Hackathon)
def deactivate_hackathon(sender, instance, **kwargs):
    if instance.end_Date <= timezone.now() and instance.active:
        instance.active = False
        instance.save(update_fields=['active'])
    

