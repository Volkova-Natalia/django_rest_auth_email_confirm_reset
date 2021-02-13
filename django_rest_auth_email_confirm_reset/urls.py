"""django_rest_auth_email_confirm_reset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .settings import end_point
from .views import (
    RegistrationView,
    LoginView,
    LogoutView,
    AuthInfoView,

    SwaggerExpectedView,
)

urlpatterns = [
    path(end_point['registration']['url'], RegistrationView.as_view(), name=end_point['registration']['name']),
    path(end_point['login']['url'], LoginView.as_view(), name=end_point['login']['name']),
    path(end_point['logout']['url'], LogoutView.as_view(), name=end_point['logout']['name']),
    path(end_point['auth_info']['url'], AuthInfoView.as_view(), name=end_point['auth_info']['name']),

    path(end_point['swagger_expected']['url'], SwaggerExpectedView.as_view(), name=end_point['swagger_expected']['name']),
]
