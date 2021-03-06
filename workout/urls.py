from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from workout.api import EjercicioViewset, RutinaViewset

router = routers.DefaultRouter()
router.register(r'ejercicio', EjercicioViewset)
router.register(r'rutina', RutinaViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]
