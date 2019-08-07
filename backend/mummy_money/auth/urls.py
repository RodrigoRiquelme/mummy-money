from django.conf.urls import url
from mummy_money.auth.views import Logout

urlpatterns = [
    url(r'^logout/', Logout.as_view()),
]
