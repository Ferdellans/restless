from django.conf.urls import url, include
from django.contrib import admin
from account.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^account/', include('account.urls')),
]
