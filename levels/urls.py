from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from levels.api import NivelViewset

router = routers.DefaultRouter()
router.register(r'nivel', NivelViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]
