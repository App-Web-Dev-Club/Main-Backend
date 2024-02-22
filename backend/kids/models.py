from django.db import models
from api.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.

class KH_Club_Members(models.Model):
    regno = models.OneToOneField(Student, on_delete = models.CASCADE, related_name='club_member')
    club_choices =[
        ('KH Core','Khacks Core Team'),
        ('3D','3D Printing Club'),
        ('AI','AI Club'),
        ('WEB AND APP','Web And App Club'),
        ('IOT AND ROBOTICS','Iot And Robotics Club'),
        ('XR','XR Club'),
        ('CYBER SECURITY','Cyber Security Club'),
        ('COMPETITIVE PROGRAMMING','Competitive Programming Club'),
        ('BUILD CLUB','Build Club'),
        ('GDSC','Google Developers Student Club'),
        # ('Neural network','Neural network '),
        ('NSN','Nvidia Student Network'),

        ('Ecell core','E-Cell Core'),
        ('Accelerator club','Accelerator Club'),
        ('Women Entrepreneur Club','Women Entrepreneurs Club'),
        ('Resource hub','Resource Hub'),
        ('Start up','Start Up Club'),

        ('Kreatives core','Kreatives Core'),
        ('TEDX','TED-X'),
        ('Design club','Design Club'),
        ('Writters club','Writers Club'),

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
    date_time = models.DateTimeField(auto_now_add=True)
    CHOICES = [
        ('Late Permission', 'Late_Night'),
        ('Night Stay Permission', 'Night_Stay'),
        ('holiday ', 'Holiday '),
    ]
    type = models.CharField(max_length=100, choices=CHOICES)


class KIDS_PunchTime(models.Model):
    name = models.CharField(max_length=255)
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
    

