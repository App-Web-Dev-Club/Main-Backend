from django.urls import path
from inventory.views import *
from kids.views import *

urlpatterns = [
    path('product', ProductAPIView.as_view(), name='Register Product Details'),
    path('product/request', ProductRequestAPIView.as_view(), name="Request to borrow a product"),
    path('product/management', ProductManagementAPIView.as_view(), name="Manage the product"),
    path('student/login', KH_Login.as_view(), name="student login (KH member)"),
    path("admin/login",AdminLogin.as_view(), name="admin login")
]