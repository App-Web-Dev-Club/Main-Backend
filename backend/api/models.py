from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, role, gender, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, role, gender, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, role, gender, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    ROLE_CHOICES = (
        ('administrator', 'Administrator'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
        ('guest', 'Guest'),
    )
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=100, choices=CHOICES)

    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role'] 





class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    register_no = models.CharField(max_length=100, unique=True)  # Ensure register_no is unique
    BRANCH_CHOICE = [
        ('Btech', 'btech'),
        ('B.Sc', 'bsc')
    ]
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICE)
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science And Engineering'),
        ('ECE', 'Electronic And Communication Engineering')
    ]

    dept = models.CharField(max_length=100 ,choice = DEPARTMENT_CHOICES)
    SCHOOL_CHOICE = [
        
    ]
    school = models.CharField(max_length=100,choice= SCHOOL_CHOICE)
    year_of_joining = models.DateField()
    year_of_studys = models.IntegerField()
    passout_year = models.DateField()
    student_status = models.BooleanField()

    


class Faculty(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    faculty_id = models.CharField(max_length=255, unique=True)
    year_of_joining = models.IntegerField()
    faculty_status = models.BooleanField()
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science And Engineering'),
        ('ECE', 'Electronic And Communication Engineering')
    ]

    dept = models.CharField(max_length=100 ,choice = DEPARTMENT_CHOICES)
    SCHOOL_CHOICE = [
        
    ]
    school = models.CharField(max_length=100,choice= SCHOOL_CHOICE)







class Attendanance_type(models.Model):
    biometric = models.BooleanField()
    face_recognition = models.BooleanField()
    barcode = models.BooleanField()

class Event(models.Model):
    event_creator = models.ForeignKey(Faculty, on_delete = models.CASCADE,related_name='events_creator')
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
    person_marked_attendanance =  models.ForeignKey(User, on_delete = models.CASCADE, related_name='attendances_marked_by')
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












