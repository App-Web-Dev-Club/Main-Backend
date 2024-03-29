
from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import *






class Attendanance_type(models.Model):
    biometric = models.BooleanField()
    face_recognition = models.BooleanField()
    barcode = models.BooleanField()

class Event(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name='events_creator')
    title = models.CharField(max_length=255)
    description = models.TextField()
    registation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    venue = models.TextField()
    type_of_attendance = models.OneToOneField(Attendanance_type, on_delete = models.CASCADE)
    accept_new_entry = models.BooleanField()
    paticipants = models.ForeignKey(User, on_delete = models.CASCADE,related_name='events_participats')
    attendanance_markers = models.ForeignKey(User, on_delete = models.CASCADE,related_name='events_attendance_marked')

    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('onprocess', 'On Process'),
        ('hold', 'Hold'),
    ]
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)

class Event_Attendanance(models.Model):
    person_marked =  models.ForeignKey(User, on_delete = models.CASCADE, related_name='attendances_marked_by')
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    paticipant = models.ForeignKey(User, on_delete = models.CASCADE,related_name='attendances_participated')
    date_time = models.DateTimeField(auto_now_add = True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class KH_Club_Members(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='club_member')
    club = models.CharField(max_length=100)#add choices
    permission = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now_add= True)
    edited_date = models.DateTimeField(auto_now=True)

class KH_Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project_lead = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE, related_name='project_led')
    kh_members = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE, related_name='project_team')

    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('onprocess', 'On Process'),
        ('hold', 'Hold'),
    ]
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)

class KH_Club_Members_Attendanance(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    word_done = models.TextField()
    project = models.ForeignKey(KH_Project, on_delete = models.CASCADE)
    user = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE, related_name='club_attendances')

class KH_Permission(models.Model):
    user = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE, related_name='permissions')
    date_time = models.DateTimeField()
    CHOICES = [
        ('late_night', 'Late_Night'),
        ('1st_year', '1st_Year'),
    ]
    type = models.CharField(max_length=100, choices=CHOICES)







