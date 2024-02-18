from django.urls import path
from inventory.views import *

urlpatterns = [
    path('product', ProductAPIView.as_view(), name='Register Product Details'),

]