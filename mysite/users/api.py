from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UsersAPI(APIView):

    """
    Lista de post (GET) y creación de usuarios(POST)
    """

    def get(self, request):
        """
        Recuperamos todos los usuarios del sistema
        :param request: HttpRequest
        :return: Response
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # Objeto response de rest_framework q se encarga de devolver los usuarios en el formato de la peticion
        return Response(serializer.data)

    def post(self, request):
        """
        Creaccion de usuarios
        :param request: HttpRequest
        :return: Response
        """
        serializer = UserSerializer(data=request.data) # en rest-framework siempre con data no con POST
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    """
    User Detail (GET), update user(PUT), delete user (DELETE)

    """
    def get(self, request, pk):
        """
        Devuelve el perfil del usuario
        :param request:
        :return:
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Actualiza usuario
        :param request: HttpRequest
        :param pk: primary key del usuario
        :return: Response
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Borra un user
        :param request: HttpRequest
        :param pk: id del user q es su pk
        :return: Response
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        user.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
