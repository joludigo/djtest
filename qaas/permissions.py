from rest_framework import permissions
from django.contrib.auth.models import Group


def check_group_permission(request, groupName: str) -> bool:
    if not request.user or not request.user.is_authenticated:
        return False
    if request.user.is_superuser:
        return True
    if request.method:
        return bool(Group.objects.get(name=groupName).user_set.filter(id=request.user.id).exists())
    return False


class IsCreator(permissions.BasePermission):
    def has_permission(self, request, view):
        res = check_group_permission(request, "creator")
        return res


class IsParticipant(permissions.BasePermission):
    def has_permission(self, request, view):
        return check_group_permission(request, "participant")
