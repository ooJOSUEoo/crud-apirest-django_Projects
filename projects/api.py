from .models import Project
from rest_framework import viewsets
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = ProjectSerializer
