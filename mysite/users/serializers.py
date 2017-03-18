from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField() # Se autogenera por eso es ReadOnlyField
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


    # Datos recibidos del Post y se encarga de parsearlos
    def create(self, validated_data):
        return self.update(User(), validated_data)

    def update(self, instance, validated_data):
        instance.firs_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


