
from django.conf.urls import url
from django.contrib import admin

from blog.views import PostsListView, BlogsListView, BlogUserView, PostUserDetail, NewPostView
from users.views import LoginView, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostsListView.as_view(), name='posts_list'),
    url(r'^blogs/$', BlogsListView.as_view(), name='blogs_list'),
    url(r'^blogs/(?P<username>[-\w]+)/$', BlogUserView.as_view(), name='blog_user'),
    url(r'^blogs/(?P<username>[-\w]+)/(?P<post_pk>[0-9]+)$', PostUserDetail.as_view(), name='post_user_detail'),
    url(r'new-post/$', NewPostView.as_view(), name="post_new"),

    # Users URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', logout, name='users_logout'),

]
# Change admin site title
admin.site.site_header = ("Wordplease Administration")
admin.site.site_title = ("Wordplease")
