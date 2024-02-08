from django.db import models

# Create your models here.
from api.models import *
from kids.models import *

class Product(models.Model):
    STATUS_CHOICES = (
        ('damaged', 'Damaged'),
        ('avaliable', 'Avaliable'),
        ('taken', 'Taken'),
    )
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_return = models.DateField()


class Manager(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    user = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE)
    taken_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField()
    STATUS_CHOICES = (
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('hold', 'Hold'),
    )
    permission_status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    product_given = models.DateField()


