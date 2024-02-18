from django.db import models

# Create your models here.
from api.models import *
from kids.models import *

class Product(models.Model):
    STATUS_CHOICES = (
        ('damaged', 'Damaged'),
        ('available', 'Available'),
        ('taken', 'Taken'),
    )
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_return = models.DateField()


class ProductRequest(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(KH_Club_Members, on_delete = models.CASCADE)
    expected_return_date = models.DateField()
    project_description = models.TextField()
    project_title = models.CharField(max_length = 255)
    STATUS_CHOICES = (
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('hold', 'Hold'),
    )
    permission_status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    



class ProductManagment(models.Model):
    request = models.ForeignKey(ProductRequest,on_delete = models.CASCADE)
    return_date = models.DateField()
    assigned_at = models.DateTimeField(auto_now_add=True)
    CONDIOTION_CHOICES = (
        ('good','Good'),
        ('damaged','Damaged')
    )
    return_condition = models.CharField(max_length=100,choices=CONDIOTION_CHOICES,null = True, default ='good')


