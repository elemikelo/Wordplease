from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        DEFINE SI UN USUARIO PUEDE USAR O NO EN EL ENDPOINT QUE QUIERE UTILIZAR
        :param request:  HttpRequest
        :param view: view PostViewSet
        :return: True si puede, False si no puede

        """
        # Si quiere ver el listado de posts
        if view.action == 'list':
            return True

        # Si quiere ver el detalle del post
        if view.action == 'retrieve':
            return True


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
        :param view: view.action ( vistas del modelo)
        :param obj: Post
        :return: True si puede, False si no puede

        """

        if view.action == 'retrieve' or 'list':
            return True

        # si es admin o el propietario del post
        if view.action == "update" or view.action == "destroy":
            if request.user.is_superuser or obj in request.user.blog.post_set.all():
                return True





