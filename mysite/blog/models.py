from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'blog_categories'


class Blog(models.Model):
    owner = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username

class Post(models.Model):

    title = models.CharField(max_length=200)
    text_introduction = models.TextField(validators=[MaxLengthValidator(500)], blank=True, null=True)
    body_post = models.TextField()
    url = models.URLField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    published_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog)

    class Meta:
        db_table = 'blog_posts'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
