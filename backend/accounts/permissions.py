from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReservationOwner(BasePermission):
    """
    Permission to only allow owners of a reservation to view or edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in SAFE_METHODS:
            return True
            
        # Write permissions are only allowed to the owner of the reservation
        return obj.user == request.user


class IsParkingLotAdmin(BasePermission):
    """
    Permission to only allow parking lot administrators to modify parking lots.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed for any authenticated user
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
            
        # Check if user is a staff member or has admin role
        return request.user and request.user.is_authenticated and (
            request.user.is_staff or 
            hasattr(request.user, 'role') and request.user.role == 'admin'
        )


class IsAccountOwner(BasePermission):
    """
    Permission to only allow users to edit their own account.
    """
    def has_object_permission(self, request, view, obj):
        # Allow users to view/edit only their own account
        return obj.id == request.user.id


class ReadOnly(BasePermission):
    """
    Permission to only allow read-only access.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS