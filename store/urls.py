from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from store.api import ProductoViewset

router = routers.DefaultRouter()
router.register(r'producto', ProductoViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]
