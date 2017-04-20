
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from blog.api import BlogsAPI, PostsViewSet
from blog.views import PostsListView, BlogsListView, BlogUserView, PostUserDetail, NewPostView
from users.views import LoginView, Register, LogoutView
from users.api import UserViewSet

router = DefaultRouter()
router.register("posts", PostsViewSet)

router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostsListView.as_view(), name='posts_list'),
    url(r'^blogs/$', BlogsListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<username>[-\w]+)/$', BlogUserView.as_view(), name='blog_user'),
    url(r'^blogs/(?P<username>[-\w]+)/(?P<post_pk>[0-9]+)$', PostUserDetail.as_view(), name='post_user_detail'),
    url(r'new-post/$', NewPostView.as_view(), name="post_new"),

    # Users URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup$', Register.as_view(), name='register'),

    # API Users
    url(r'^api/1.0/', include(router.urls)),

    # API Blogs
    url(r'^api/1.0/blogs/$', BlogsAPI.as_view(), name='blogs_api'),

    # API Posts
    url(r'^api/1.0/', include(router.urls)),

]
# Change admin site title
admin.site.site_header = ("Wordplease Administration")
admin.site.site_title = ("Wordplease")
