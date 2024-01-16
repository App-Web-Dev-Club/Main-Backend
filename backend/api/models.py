from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    permission = models.CharField(max_length=255, default="")
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Attendanance_type(models.Model):
    biometric = models.BooleanField()
    face_recognition = models.BooleanField()
    barcode = models.BooleanField()

class Event(models.Model):
    user = models.ForeignKey(User)
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
    type_of_attendance = models.OneToOneField(Attendanance_type)
    accept_new_entry = models.BooleanField()
    paticipantss = models.ForeignKey(User)
    attendanance_markers = models.ForeignKey(User)
    Status = models.CharField(max_length=255)


