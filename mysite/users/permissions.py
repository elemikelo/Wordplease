from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    my_safe_permission = ['GET', 'PUT', 'DELETE']

    def has_permission(self, request, view):
        """
        DEFINE SI UN USUARIO PUEDE USAR O NO EN EL ENDPOINT QUE QUIERE UTILIZAR
        :param request:  HttpRequest
        :param view: UserApi/UserDetailAPI
        :return: True si puede, False si no puede
        """
        # Post Create --> cualquiera

        if request.method == 'POST':
            return True

        # GET Detail, --> Superuser or sameUser
        if request.user.is_authenticated and request.method in self.my_safe_permission:
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
        # Permisos --> admin sobre si mismo o administrador
        return request.user.is_superuser or request.user == obj