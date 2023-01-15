from .api import UserAPI
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/v1/users/',UserAPI.as_view(), name='users'),
    path('api/v1/users/token/', obtain_auth_token, name='token'),
    path('api/v1/users/<int:pk>/',UserAPI.as_view(), name='users'),
]