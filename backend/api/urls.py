from django.urls import path
# from .views import RegisterView, LoginView,TestView,RefreshTokenView
from .views import *
from kids.views import *
urlpatterns = [

    # migrated from prototype -------------------------
    
    path('projects', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('userid',Userid.as_view(),name='get userid using regno used for both project and attendance'),
    path('userid/projects',project_under_user.as_view(),name='get project from userid used for attendance'),
    path('attendance', AttendanceListCreateAPIView.as_view(), name='attendance-list-create'),
    path('process',PermissionView.as_view()),
    # path('face',FaceAttendanceListCreateAPIView.as_view()),
    path('punch', PunchTimeView.as_view()),
    # path('punchtime/sort',PunchTimeGETView.as_view()),
    # path('send-email/', SendEmailView.as_view(), name='send-email'),

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


]