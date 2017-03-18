from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post
from blog.serializers import PostSerializer


class PostsAPI(APIView):
    """
    List(GET) and creates(POST) Post
    """

    def get(self, request):

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)