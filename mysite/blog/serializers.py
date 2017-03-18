from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

    # Con este modelo serializer ya implementa la funcion create, update, validate