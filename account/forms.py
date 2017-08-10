from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _

from account.models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'type', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'example@gmail.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'больше 6 символов'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'пароль еще раз'})

        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Пвоторить пароль'


class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Email'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
