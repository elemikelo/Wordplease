from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Post, Blog
from blog.serializers import PostSerializer, BlogSerializer, PostsListSerializer
from blog.views import PostQuerySet


class BlogsAPI(ListAPIView):
    """
    Listado de Blog de la plataforma
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class PostsAPI(PostQuerySet, ListCreateAPIView):
    """
    Listado de posts(GET) y creacion de un post(POST)
    """
    queryset = Post.objects.all().values("title", "url", "text_introduction", "published_date").order_by('-published_date')
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PostsListSerializer if self.request.method == "GET" else PostSerializer

    def get_queryset(self):
        return self.get_post_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(blog=self.request.user.blog)



class PostDetailAPI(PostQuerySet, RetrieveUpdateDestroyAPIView):
    """
    Recuperacion actualizacion y borrado de un post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_post_queryset(self.request)







