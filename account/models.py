from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if not email:
            raise ValueError('Users must have a valid email address.')

        account = self.model(email=self.normalize_email(email))
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password):
        account = self.create_user(email, password)
        account.is_admin = True
        account.save()
        return account


class Account(AbstractBaseUser):
    class Meta:
        verbose_name_plural = 'Пользователи'

    email = models.EmailField('E-mail', unique=True, null=True)

    TYPE = (
        (1, 'first'),
        (2, 'second'),
    )
    type = models.IntegerField(choices=TYPE, default=1)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return str()

    def get_short_name(self):
        return str()

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
