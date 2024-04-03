from rest_framework import permissions


class ReadOnlyIfNotAuthenticatedOrOwner(permissions.BasePermission):

  def has_permission(self, request, view):
    # 익명 사용자에게는 읽기 권한만 부여됩니다.
    if not request.user.is_authenticated:
        return request.method in permissions.SAFE_METHODS
    # 인증된 사용자에게는 읽기 및 쓰기 권한이 부여됩니다.
    return True

  def has_object_permission(self, request, view, obj):
    # 수정 및 삭제는 객체의 소유자에게만 허용됩니다.
    return (request.user == obj.user or request.user.is_staff)