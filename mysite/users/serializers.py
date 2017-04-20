from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RelatedObjectDoesNotExist(object):
    pass


class RegisterSerializer(UserSerializer):
    blog_name = serializers.CharField()

    class Meta(UserSerializer.Meta):
        pass

    def update_user_with_blog_info(self, user, blog_name):
        try:
            user.blog.name = blog_name
            user.blog.save()
            user.blog_name = blog_name
        except Blog.DoesNotExist:
            Blog.objects.create(owner=user, name=blog_name)
            user.blog_name = blog_name
        return user

    def extract_blog_data_and_encrypt_password(self, validated_data):
        blog_name = validated_data.pop('blog_name')
        password = validated_data.get('password')
        if password:
            validated_data['password'] = make_password(password)
        validated_data['is_active'] = True
        return (blog_name)

    def create(self, validated_data):
        """
        Extrae los datos del blog de datos validados, crea al usuario y luego crea el blog

        """
        blog_name = self.extract_blog_data_and_encrypt_password(validated_data)
        user = super(UserSerializer, self).create(validated_data)
        if user:
            self.update_user_with_blog_info(user, blog_name)
        return user

    def update(self, instance, validated_data):
        """
        Extrae los datos del blog de datos validados, crea al usuario y luego crea el blog

        """
        blog_name = self.extract_blog_data_and_encrypt_password(validated_data)
        user = super(UserSerializer, self).update(instance, validated_data)
        self.update_user_with_blog_info(user, blog_name)
        return user


