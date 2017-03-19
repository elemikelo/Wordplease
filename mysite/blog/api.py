from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blog.models import Post, Blog
from blog.permissions import UserPermission
from blog.serializers import PostSerializer, BlogSerializer, PostsListSerializer
from blog.views import PostQuerySet


class BlogsAPI(ListAPIView):
    """
    Listado de Blog de la plataforma
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('owner__username',)
    ordering_fields = ('name',)



class PostsViewSet(PostQuerySet, ModelViewSet):
    """
    Modelo que incluye todos los Endpoints
    """
    queryset = Post.objects.all().order_by('-published_date')
    permission_classes = (UserPermission,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'body_post')
    ordering_fields = ('title', 'published_date')


    def get_serializer_class(self):
        return PostsListSerializer if self.action == "list" else PostSerializer

    def get_queryset(self):
        return self.get_post_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(blog=self.request.user.blog)




