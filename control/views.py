from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views import View


class SignUp(View):
    def get(self, request):
        return render(request, 'control/signup.html', {
            'form': UserCreationForm
        })

    def post(self, request):
        post = request.POST
        if post['password1'] == post['password2']:
            try:
                user = User.objects.create_user(
                    username=post['username'],
                    password=post['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'control/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'control/signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })


class SignIn(View):
    def get(self, request):
        return render(request, 'control/signin.html', {
            'form': AuthenticationForm
        })

    def post(self, request):
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            return render(request, 'control/signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña no existe'
            })

        login(request, user)

        # 🔑 Manejar el parámetro ?next=
        next_url = request.GET.get('next') or request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('home')


class SignOut(View):
    def get(self, request):
        logout(request)
        return redirect('home')
