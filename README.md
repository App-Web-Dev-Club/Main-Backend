api - contain user and event details (if possible split both of them)
kids - contain details about the clubs attendanance
inventory - contain hardwares in kids 


APIs that needs fixing: (these are under KIDS)
            --> path('attendance', AttendanceListCreateAPIView.as_view(), name='attendance-list-create'),
            --> path('process',PermissionView.as_view()),
            --> # path('face',FaceAttendanceListCreateAPIView.as_view()),
            --> path('punch', PunchTimeView.as_view()),
            --> path("memberlogin", KH_Club_MembersLoginView.as_view())
            --> # path('punchtime/sort',PunchTimeGETView.as_view()),
            --> # path('send-email/', SendEmailView.as_view(), name='send-email'),



make it more modularise so it would be easy to maintain.