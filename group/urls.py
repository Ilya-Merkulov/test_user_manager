from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^group/$', views.group),
    url(r'^group/([0-9]+)$', views.group),
]