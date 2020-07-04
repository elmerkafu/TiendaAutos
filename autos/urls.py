from django.urls import path, include
from rest_framework import routers
from .views import TipoView, MarcaView, ModeloView, AutoView, login, InsertAuto, InsertModelo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


router = routers.DefaultRouter()
router.register('tipo', TipoView)
router.register('marca', MarcaView)
router.register('modelo', ModeloView)
router.register('auto', AutoView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login', login, name="login"),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("insert_auto/", login_required(InsertAuto.as_view()), name="insert.auto"),
    path("insert_modelo/", InsertModelo.as_view(), name="insert.modelo")
]
