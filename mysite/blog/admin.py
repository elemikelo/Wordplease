from django.contrib import admin
from blog.models import Post, Blog, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner', 'created_at', 'modified_at')
    list_filter = ('owner',)
    search_fields = ('owner',)


admin.site.register(Post)
admin.site.register(Category)