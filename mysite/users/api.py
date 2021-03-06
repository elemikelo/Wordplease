from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from users.permissions import UserPermission
from users.serializers import UserSerializer, RegisterSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    def get_serializer_class(self):
        """
        Returns SinupSerializer when trying to create a new user
        """
        return RegisterSerializer if self.action in ['create', 'update'] else UserSerializer




