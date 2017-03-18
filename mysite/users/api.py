from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from users.permissions import UserPermission
from users.serializers import UserSerializer


class UsersAPI(CreateAPIView):
    """
    Endpoint creación de usuarios(POST)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint Recuperacion actualizacion y borrado de Usuario
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)




