from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomPermission(permissions.BasePermission):
    def isAdmin(self, request):
        return bool(request.user.role == 'admin')

    def isTeacher(self, request):
        return bool(request.user.role == 'teacher')
