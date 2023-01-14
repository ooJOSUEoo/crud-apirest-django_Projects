from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView

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