
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from blog.api import PostsAPI, BlogsAPI, PostDetailAPI
from blog.views import PostsListView, BlogsListView, BlogUserView, PostUserDetail, NewPostView
from users.views import LoginView, Register, LogoutView

#from users.api import UserViewSet
from users.api import UsersAPI, UserDetailAPI

#from blog.api import BlogsViewSet
#from blog.api import PostsViewSet



#router = DefaultRouter()
#router.register("users", UsersAPI, base_name="users_api")
#router.register("blogs", BlogsViewSet)
#router.register("posts", PostsViewSet)

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
    #url(r'^api/1.0/', include(router.urls)),
    url(r'^api/1.0/users/$', UsersAPI.as_view(), name='users_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)/?$', UserDetailAPI.as_view(), name='users_detail_api'),

    # API Blogs
    url(r'^api/1.0/blogs/$', BlogsAPI.as_view(), name='blogs_api'),

    # API Posts
    url(r'^api/1.0/posts/$', PostsAPI.as_view(), name='posts_api'),
    url(r'^api/1.0/posts/(?P<pk>[0-9]+)/$', PostDetailAPI.as_view(), name='post_detail_api'),


]
# Change admin site title
admin.site.site_header = ("Wordplease Administration")
admin.site.site_title = ("Wordplease")
