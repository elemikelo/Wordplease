from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as django_logout, login as django_login
from django.views import View

from users.forms import LoginForm


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



def logout(request):
    """
    Logout de un usuario
    :param request: HttpRequest
    :return: HttpResponse
    """
    django_logout(request)
    return redirect('posts_list')

