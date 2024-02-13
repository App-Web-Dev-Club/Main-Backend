from rest_framework.permissions import BasePermission

class IsKH_Club_Members(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.permission == 'MEMBER' or request.user.permission == 'CLUB_LEADER'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin' 