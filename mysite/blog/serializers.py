from rest_framework import serializers
from rest_framework.reverse import reverse

from blog.models import Post, Blog

class BlogSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()

    def get_url(self, blog):
        request = self.context.get("request")
        return request.get_host() + reverse('blog_user', args=[blog.owner])

    class Meta:
            model = Blog
            fields = ["id", "name", "url"]



class PostsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", "title", "url", "text_introduction", "published_date"]

class PostSerializer(serializers.ModelSerializer):


    class Meta:
        model = Post
        fields = "__all__"

