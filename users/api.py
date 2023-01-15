from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User

class UserAPI(APIView):
    # que no necesite autenticacion
    authentication_classes = ()
    permission_classes = ()
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request, pk=None, format=None):
    #     print(pk)
    #     if pk:
    #         user = User.objects.get(pk=pk)
    #         serializer = UserSerializer(user)
    #     else:
    #         users = User.objects.all()
    #         serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    # def delete(self, request, pk, format=None):
    #     if pk:
    #         user = User.objects.get(pk=pk)
    #         user.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def put(self, request, pk, format=None):
    #     if pk:
    #         user = User.objects.get(pk=pk)
    #         serializer = UserSerializer(user, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)