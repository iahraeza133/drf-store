from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to grant full access to admin users,
    and read-only access to others.
    """
    def has_permission(self, request, view):
        # Admin users have full access
        if request.user and request.user.is_staff:
            return True
        
        # Read-only access for non-admin users
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        
        # Deny access for non-admin users who are trying to modify data (POST, PUT, DELETE, etc.)
        return False
