from rest_framework.permissions import BasePermission, SAFE_METHODS


SUPPORT_APP_SAFE_METHODS = ('GET', 'POST', 'HEAD', 'OPTIONS')


class IsStaffOrQuestionOnly(BasePermission):
    def has_permission(self, request, view):
        return bool((request.user and request.user.is_authenticated and request.method in SUPPORT_APP_SAFE_METHODS)
                    or request.user.is_staff)


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool((request.user and request.user.is_authenticated and request.method in SAFE_METHODS)
                    or request.user.is_staff)


