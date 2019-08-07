from django.conf.urls import url, include
from rest_framework import routers

from mummy_money.investors.views import PyramidViewSet

router = routers.DefaultRouter()
router.register(r'investors', PyramidViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
