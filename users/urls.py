from .api import UserAPI
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/v1/user/create_user/', UserAPI.as_view(), name='create_user'),
    path('api/v1/user/token/', obtain_auth_token, name='token'),
]