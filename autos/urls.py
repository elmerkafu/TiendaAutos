from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from . import views
from .views import InsertAuto, InsertModelo

urlpatterns = [
    path("", views.home, name="index"),
    path("login", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("insert_auto/", InsertAuto.as_view(), name="insert.auto"),
    path("insert_modelo/", InsertModelo.as_view(), name="insert.modelo")
]

