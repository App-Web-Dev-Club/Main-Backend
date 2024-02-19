from django.urls import path
# from .views import *
from kids.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('projects', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('userid',Studentid.as_view(),name='get userid using regno used for both project and attendance'),
    path('userid/projects',project_under_user.as_view(),name='get project from userid used for attendance'),
    path('attendance', AttendanceListCreateAPIView.as_view(), name='attendance-list-create'),
    path('permission',PermissionView.as_view()),
    # path('face',FaceAttendanceListCreateAPIView.as_view()),
    path('punch', PunchTimeView.as_view()),
    path('punchtime/sort',PunchTimeGETView.as_view()),
    path('login/', KH_Login.as_view(), name='send-email'),
    path('hackathon', HackathonAPIView.as_view(), name="This is hackathon register site")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

