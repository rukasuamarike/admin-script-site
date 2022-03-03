"""p2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include,path
from pages.views import (home_view,hello_world,panel,log,new_user,shell_send,accountinfo)

urlpatterns = [

    url(r'^admin/shell/', include('django_admin_shell.urls')),
    url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', home_view),
    path('logs/', log),
    path('shellsend/', shell_send),
    path('panel/', panel),
    path('hello/', hello_world),
    path('newuser/', new_user),
    path('main/', include('main.urls')),
    path('account/',accountinfo)

]
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='main/', permanent=True)),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

