from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        DEFINE SI UN USUARIO PUEDE USAR O NO EN EL ENDPOINT QUE QUIERE UTILIZAR
        :param request:  HttpRequest
        :param view: UserApi/UserDetailAPI
        :return: True si puede, False si no puede
        """
       # cualquiera autentica puede acceder al detalle para ver , actualizar o borrar

        if request.user.is_authenticated and view.action in ("retrieve", "update", "destroy"):
            return True

        # si es superadmin y quiere acceder al listado
        if request.user.is_superuser and view.action == "list":
            return True

        # cualquier puede crear un usuario (POST)

        if view.action == "create":
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
        # si es admin o es el mismo le dejamos

        return request.user.is_superuser or request.user == obj