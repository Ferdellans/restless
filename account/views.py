from django.contrib import messages, auth
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from restless.views import Endpoint
from restless.modelviews import DetailEndpoint
from restless.auth import AuthenticateEndpoint

from account.forms import RegisterForm, LoginForm
from account.models import Account


def index(request):
    return render(request, 'index.html')


class Register(DetailEndpoint):
    model = Account
    form = RegisterForm()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.error(request, 'Вы авторизированы')
            return redirect('/')
        return render(request, 'account/register.html', {'form': self.form})

    def post(self, request, *args, **kwargs):
        self.form = RegisterForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            messages.success(request, 'Удачно зареган, войдите')
            return redirect('/account/login')
        return render(request, 'account/register.html', {'form': self.form})


class Login(AuthenticateEndpoint):
    user_fields = ('email', 'password')
    form = LoginForm()

    def get(self, request, *args, **kwargs):
        return render(request, 'account/login.html', {'form': self.form})

    def post(self, request, *args, **kwargs):
        self.form = LoginForm(request.POST)

        if self.form.is_valid():

            email = self.form.cleaned_data['email']
            password = self.form.cleaned_data['password']
            user = auth.authenticate(username=email, password=password)
            # user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Добро пожаловать, %s!' % request.user)
                return redirect('/')

            messages.error(request, 'Неправильный пароль или почта')
            return redirect('/account/login/')


class Logout(Endpoint):
    def get(self, request):
        logout(request)
        messages.success(request, 'Удачи')
        return redirect('/')
