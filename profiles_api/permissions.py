from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""
    
    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile."""
        
        # If the request is a safe method, then it is allowed.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Otherwise, check if the user is trying to edit their own profile.
        return obj.id == request.user.id