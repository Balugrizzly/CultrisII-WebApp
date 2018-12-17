from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('download', views.download, name="download"),
    path('register', views.register, name="register"),
    path('signin', views.sign_in, name="sign_in"),
]
