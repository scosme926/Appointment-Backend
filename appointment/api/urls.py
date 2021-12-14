from django.urls import path
from . import views


urlpatterns = [
    path('version', views.version_endpoint, name='version_endpoint'),
    path('hello', views.hello_endpoint, name='hello_endpoint'),

]
