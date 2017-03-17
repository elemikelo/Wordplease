
from django.conf.urls import url
from django.contrib import admin

from blog.views import PostsListView, BlogsListView, BlogUserView, PostUserDetail, NewPostView
from users.views import LoginView, Register, LogoutView

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

]
# Change admin site title
admin.site.site_header = ("Wordplease Administration")
admin.site.site_title = ("Wordplease")
