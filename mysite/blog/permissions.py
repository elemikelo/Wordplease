from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        DEFINE SI UN USUARIO PUEDE USAR O NO EN EL ENDPOINT QUE QUIERE UTILIZAR
        :param request:  HttpRequest
        :param view: view PostViewSet
        :return: True si puede, False si no puede

        """
        # Si está autenticado puede crear el post
        if request.user.is_authenticated and view.action == "create":
            return True

        # Si está autenticado puede actualizar y borrar el post
        if request.user.is_authenticated and view.action in ("update", "destroy"):
            return True

        return False


    def has_object_permission(self, request, view, obj):
        """
        define si el usuario  puede realizar la accion sobre el objeto que quiere realzarla
        :param request: HttpRequest
        :param view: UserApi/UserDetailAPI
        :param obj: User
        :return: True si puede, False si no puede
        """
        # si es admin o el propietario del post
        return request.user.is_superuser or request.user == obj



