from rest_framework import serializers

from blog.models import Post, Blog


class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "url", "text_introduction", "published_date"]

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ["name",]

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

    # Con este modelo serializer ya implementa la funcion create, update, validate