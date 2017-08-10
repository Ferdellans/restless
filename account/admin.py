from django.contrib import admin
from account.models import Account


class Accounts(admin.ModelAdmin):
    class Meta:
        model = Account

    list_display = ['id', 'email', 'type', 'created_at']


admin.site.register(Account, Accounts)
