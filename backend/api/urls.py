from django.urls import path
from .views import RegisterView, LoginView,TestView,RefreshTokenView,GoogleLogin
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('refresh', RefreshTokenView.as_view()),








    path('auth/google/', GoogleLogin.as_view(), name='google-login'),
    path('hello', TestView.as_view()),


]