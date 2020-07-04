from django.urls import path, include
from rest_framework import routers
from .views import TipoView, MarcaView, ModeloView, AutoView, login
from .views import InsertAuto, InsertModelo, InsertMarca, InsertTipo, home
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


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
    path("insert_modelo/", login_required(InsertModelo.as_view()), name="insert.modelo"),
    path("insert_marca/", login_required(InsertMarca.as_view()), name="insert.marca"),
    path("insert_tipo/", login_required(InsertTipo.as_view()), name="insert.tipo"),
    path("", login_required(home), name="index")
]
