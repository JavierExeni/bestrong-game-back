from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from authentication.api import UserViewset, BodyInfoViewset

router = routers.DefaultRouter()
router.register(r'user', UserViewset)
router.register(r'bodyInfo', BodyInfoViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]