from django.urls import path
# from .views import RegisterView, LoginView,TestView,RefreshTokenView
from .views import *
from kids.views import *
urlpatterns = [

    # migrated from prototype -------------------------
    
    

    #--------------------------------


    # path('register', RegisterView.as_view()),
    # path('login', LoginView.as_view()),
    # path('refresh', RefreshTokenView.as_view()),

    path('register/', UserRegistrationView.as_view(), name='guest-registration'),
    path('login/', UserLoginView.as_view(), name='guest-login'),

    path('register/student/', StudentRegistrationView.as_view(), name='student-registration'),
    path('login/student/', StudentLoginView.as_view(), name='student-registration'),

    path('register/faculty/', FacultyRegistrationView.as_view(), name='faculty-registration'),
    path('login/faculty/', FacultyLoginView.as_view(), name='faculty-registration'),

    path('logout/', UserLogoutView.as_view(), name='logout'),
    ################  Registation Login Logout #######################



    # # path('ttt',register_by_access_token),
    path('test', TestView.as_view()),
    path('login-with-google/',LoginWithGoogle.as_view(), name='google'),  

    path('login/admin/',Admin_Login.as_view(), name="admin login")

]