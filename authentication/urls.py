from django.urls import re_path, include

from .views import RegistrationAPIView
from .views import LoginAPIView, UserRetrieveUpdateDestroyAPIView
from . import views
# from .views import UserRetrieveUpdateAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^user/$', views.user),
    url(r'^user/([0-9]+)$', views.user),
    #re_path(r'^users/', ListOfUsers.as_view(), name='get_users'),
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^login/user/?$', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_login'),
   
]