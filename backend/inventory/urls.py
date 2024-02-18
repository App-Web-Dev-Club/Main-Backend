from django.urls import path
from inventory.views import *

urlpatterns = [
    path('product', ProductAPIView.as_view(), name='Register Product Details'),
    path('product/request', ProductRequestAPIView.as_view(), name="Request to borrow a product"),
]