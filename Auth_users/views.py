from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from propiedades2.models import Staff


def auth_login(request):
    template_name = 'login.html'
    data = {}
    username = password = ''
    if request.user.is_active == False:
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(
                username=username,
                password=password
                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    print("usuario o contraseña no validos")
                    messages.warning(
                        request,
                        'Usuario o contraseña incorrectos!'
                        )
            else:
                print("Usuario incorrecto")
                messages.error(
                    request,
                    'Usuario o contraseña incorrectos!'
                    )
        return render(request, template_name, data)
    else:
        data['staff'] = Staff.objects.get(username_staff=request.user)
        return render(request, 'index.html', data)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('LOGIN'))
