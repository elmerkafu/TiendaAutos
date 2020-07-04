from django.urls import path, include
from rest_framework import routers
from .views import TipoView, MarcaView, ModeloView, AutoView


router = routers.DefaultRouter()
router.register('tipo', TipoView)
router.register('marca', MarcaView)
router.register('modelo', ModeloView)
router.register('auto', AutoView)

urlpatterns = [
    path('api/', include(router.urls))
]
