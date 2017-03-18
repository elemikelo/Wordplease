from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Post, Blog
from blog.serializers import PostSerializer, BlogSerializer, PostsListSerializer


class BlogsAPI(ListAPIView):
    """
    Listado de Blog de la plataforma
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class PostsAPI(ListCreateAPIView):
    """
    Listado de posts(GET) y creacion de un post(POST)
    """
    queryset = Post.objects.all().values("title", "url", "text_introduction", "published_date").order_by('-published_date')
    serializer_class = PostSerializer

    def get_serializer_class(self):
        return PostsListSerializer if self.request.method == "GET" else PostSerializer

class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Recuperacion actualizacion y borrado de un post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

