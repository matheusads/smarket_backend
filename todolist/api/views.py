from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, TaskSerializer
from .models import TaskModel


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TaskViewSet(ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
