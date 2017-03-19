from rest_framework import serializers
from rest_framework.reverse import reverse

from blog.models import Post, Blog

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
            model = Blog
            fields = ["name",]



class PostsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["title", "url", "text_introduction", "published_date"]

class PostSerializer(serializers.ModelSerializer):


    class Meta:
        model = Post
        fields = "__all__"

