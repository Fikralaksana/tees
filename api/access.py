from rest_framework import permissions

class IsPenjual(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.penjual
            return True
        except:
            return False

