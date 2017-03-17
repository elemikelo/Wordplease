from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as django_logout, login as django_login
from django.views import View

from blog.models import Blog
from users.forms import LoginForm, RegisterForm


class LoginView(View):

    def get(self, request):
        """
        Carga formulario login al usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = {
            'form': LoginForm()
        }
        return render(request, 'blog/login.html', context)

    def post(self, request):
        """
        Login de un user
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = LoginForm(request.POST)
        context = dict()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # usuario autenticado
                request.session["default-language"] = "es"
                django_login(request, user)
                url = request.GET.get('next', 'posts_list')
                return redirect(url)
            else:
                # usuario no autenticado
                context['error'] = "Username o password incorrecta"
        context["form"] = form
        return render(request, 'blog/login.html', context)


class LogoutView(View):

    def get(self, request):
        """
        Logout de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        django_logout(request)
        return redirect('posts_list')


class Register(View):

    def get(self, request):
        """
        Carga formulario login al usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = {
            'form': RegisterForm()
        }
        return render(request, 'blog/register.html', context)


    def post(self, request):

        """
        Registro de un user
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = RegisterForm(request.POST)
        context = dict()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(username=username, email=email)

            except User.DoesNotExist:

                # Creo usuario
                new_user = User.objects.create_user(username, email, password)

                # Añado otra información
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()

                # Hago Login
                django_login(request, new_user)

                # Creo blog al registrar con el nombre del usuario
                new_blog = Blog()
                new_blog.name = username # nombre por defecto
                new_blog.owner = request.user
                new_blog.save()

                url = request.GET.get('next', 'posts_list')
                return redirect(url)

            else:
                context["form"] = form
                context['error'] = "Usuario ya registrado"

            return render(request, 'blog/register.html', context)





