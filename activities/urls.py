from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from activities.api import LeccionViewset, ActividadViewset, OpcionViewset

router = routers.DefaultRouter()
router.register(r'leccion', LeccionViewset)
router.register(r'actividad', ActividadViewset)
router.register(r'opcion', OpcionViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]
