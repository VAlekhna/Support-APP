from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or request.user.is_staff)
# Добавить новую модель ответов, связать ответы со стафом или с автором вопроса.


# class IsStaffOrAuthorOnly(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # return bool(
#         #     request.method in SAFE_METHODS or
#         #     request.user and
#         #     request.user.is_authenticated and request.user.is_staff
#         # ) obj.author == request.user or
#         return bool(request.user.is_staff)
