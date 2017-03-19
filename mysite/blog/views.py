from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.generics import get_object_or_404
from blog.forms import PostForm
from blog.models import Post, Blog, PUBLIC


# Si el usuario esta autenticado y es super usuario todos los posts
# Si esta autenticado los post suyos y los publicos de otros
# Si no esta autenticado solo las publicas

class PostQuerySet(object):
    def get_post_queryset(self, request):
        if not request.user.is_authenticated():
            posts = Post.objects.filter(privacy=PUBLIC).order_by('-published_date')
        elif request.user.is_superuser:
            posts = Post.objects.all().order_by('-published_date')
        else:
            posts = Post.objects.filter(Q(blog=request.user.blog) | Q(privacy=PUBLIC)).order_by('-published_date')
        return posts


class PostsListView(View, PostQuerySet):

    #@method_decorator(login_required)

    def get(self, request):

        """
        Recupera todos los post de la plataforma
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = {
            'post_objects': self.get_post_queryset(request)[:20]
        }

        return render(request, 'blog/list_posts.html', context)

class BlogsListView(View):

    @method_decorator(login_required)

    def get(self, request):

        """
        Recupera el listado de blogs de los usuarios que hay en la plataforma
        :param request: HttpRequest
        :return: HttpResponse

        """
        blogs = Blog.objects.all().values("name")

        context = {
            'blog_objects': blogs
        }

        return render(request, 'blog/list_blogs.html', context)

class BlogUserView(View):

    @method_decorator(login_required)

    def get(self, request, username):

        """
        Recupera todos los post del usuario autenticado
        :param request: HttpResponse
        :param username: nombre de usuario
        :return: HttpResponse(render)
        """
        if request.user.blog.owner.username == username or request.user.is_superuser:
            posts = Post.objects.filter(blog=request.user.blog).order_by('-published_date')
        else:
            try:
                user = User.objects.get(username=username).id
                posts = Post.objects.filter(privacy=PUBLIC, blog=user).order_by('-published_date')
            except User.DoesNotExist:
                return render(request, '404.html', {}, status=404)



        context = {
            'post_objects': posts[:20] #limitado
        }

        return render(request, 'blog/blog_user.html', context)



class PostUserDetail(View, PostQuerySet):

    @method_decorator(login_required)

    def get(self, request, username, post_pk):
        """
        Carga la pagina de detalle de un post
        :param request: HttpRequest
        :param username:  nombre de usuario
        :param post_pk: id del post
        :return: HttpResponse
        """
        try:
            user = User.objects.select_related().get(username=username).id
            post = Post.objects.select_related().get(blog=user, pk=post_pk)

        except Post.DoesNotExist:
            return render(request, '404.html', {}, status=404)
        except User.DoesNotExist:
            return render(request, '404.html', {}, status=404)
        except Post.MultipleObjectsReturned:
            return render("Existen varios post con ese identificador", status=300)

        context = {
            'post': post
        }
        return render(request, 'blog/post_detail.html', context)


class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):

        # Crear formulario
        form = PostForm()

        # Renderizar plantilla
        context = {
            "form": form
        }
        return render(request, 'blog/new.html', context)

    @method_decorator(login_required)
    def post(self, request):

        # Crear formulario

        post_with_blog = Post(blog=request.user.blog)

        form = PostForm(request.POST, instance=post_with_blog)

        # validar formulario
        if form.is_valid():
            post = form.save()

            # mensaje de exito
            message = 'Post creado con éxito! <a href="{0}">Ver Post</a>'.format(
                reverse('post_user_detail', args=[request.user.username, post.pk])  # genera la URL de detalle del post
            )
            form = PostForm()
        else:
            # Mensaje de error
            message = "Se ha producido un error"

        # Renderizar plantilla
        context = {
            "form": form,
            "message": message
        }
        return render(request, 'blog/new.html', context)



