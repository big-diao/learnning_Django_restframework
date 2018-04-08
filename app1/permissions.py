from rest_framework import permissions



class BlacklistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        ip = request.META['REMOTE_ADDR']
        print(ip)
        blacklisted = ip in ['127.0.0.10',]
        return  not blacklisted

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.method in permissions.SAFE_METHODS:
            return  False
        print('IsOwnerOrReadOnly')
        return obj.owner == request.user

