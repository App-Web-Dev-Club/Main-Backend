from rest_framework.permissions import BasePermission

class IsFaculty(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'faculty'

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'student'

class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'guest'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'
