#encoding: utf-8

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.urls.base import reverse_lazy

@login_required(login_url=reverse_lazy('login'))
def home(request):
    return redirect(reverse_lazy('contractors:list_contractors'))

def app_login(request):

    logout(request)
    username = password = ''
    error = False

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('contractors:list_contractors'))

                error = 'Usuario no activo'
            else:
                error = 'Credenciales no válidas'
        else:
            error = 'Usuario y contraseña requeridos'
    return render(request, 'login.html', {'error':error, 'site_user':username})


def app_logout(request):
    logout(request)
    return redirect(reverse_lazy('login'))
