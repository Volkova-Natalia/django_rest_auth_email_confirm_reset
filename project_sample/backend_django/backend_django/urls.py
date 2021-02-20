"""backend_django URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from .settings import WORK_STAGE

urlpatterns = [
    path('admin/', admin.site.urls),
]

if WORK_STAGE != "test_before_packaging":
    urlpatterns.append(path('auth/', include(('django_rest_auth_email_confirm_reset.urls', 'django_rest_auth_email_confirm_reset'), namespace='auth')))
    # urlpatterns.append(path('auth/', include('django_rest_auth_email_confirm_reset.urls')))
