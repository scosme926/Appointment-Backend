from django.urls import path
from . import views


urlpatterns = [
    path('version', views.version_endpoint, name='version_endpoint'),
    path('hello', views.hello_endpoint, name='hello_endpoint'),
    path('login', views.login_endpoint, name="login_endpoint"),
    path('register', views.register_endpoint, name="register_endpoint"),
]
