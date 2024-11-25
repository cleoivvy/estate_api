from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsUser(BasePermission):
    
    
    def has_permission(self, request, view):
        
        if request.user.is_authenticated and request.user.role == 'user' :
            return True
        else:
            raise PermissionDenied('You are not authourized to access this resource')