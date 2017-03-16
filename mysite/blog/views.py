from audioop import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from blog.forms import PostForm
from blog.models import Post, Blog

class PostsListView(View):

    @method_decorator(login_required)

    def get(self, request):

        """
        Recupera todos los post
        :param request: HttpRequest
        :return: HttpResponse
        """
        # Todos los posts

        posts = Post.objects.all()

        # Los ultimos publicados

        posts = Post.objects.order_by('-published_date')

        context = {
            'post_objects': posts[:10]
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
        blogs = Blog.objects.all()

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

        u = User.objects.filter(username=username).select_related()
        b = Blog.objects.filter(owner=u).select_related()

        if len(u) > 0 and len(b) > 0:
            posts = Post.objects.order_by('-published_date').filter(blog=b).select_related()
            context = {
                'post_objects': posts[:20]
            }
            return render(request, 'blog/blog_user.html', context)
        else:
            return render(request, '404.html', {}, status=404)


class PostUserDetail(View):

    @method_decorator(login_required)

    def get(self, request, username, post_pk):

        """
        Carga la pagina de detalle de un post
        :param request: HttpRequest
        :param username:  nombre de usuario
        :param post_pk: id del post
        :return: HttpResponse
        """
        # a partir del username en la url saco el id del blog que a su vez está relacionado al propietario del post

        u = User.objects.filter(username=username).select_related()
        b = Blog.objects.filter(owner=u).select_related()

        if len(u) > 0 and len(b) > 0:
            try:
                post = Post.objects.select_related().get(blog=b, pk=post_pk)
            except Post.DoesNotExist:
                return render(request, '404.html', {}, status=404)
            except Post.MultipleObjectsReturned:
                return render("Existen varios post con ese identificador", status=300)

            context = {
                'post_user_detail': post
            }
            return render(request, 'blog/post_detail.html', context)
        else:
            return render(request, '404.html', {}, status=404)

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
        u = User.objects.filter(id=request.user.id).select_related()
        b = Blog.objects.select_related().get(owner=u).id
        post_with_user = Post(blog_id=b)

        form = PostForm(request.POST, instance=post_with_user)

        # validar formulario
        if form.is_valid():
            post = form.save()

            # mensaje de exito
            message = 'Post creado con éxito'
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



