from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """
    Проверка прав доступа для активного пользователя.
    """

    def has_permission(self, request, view):
        return request.user.is_active
