from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, TaskSerializer
from .models import TaskModel
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class TaskViewSet(ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        if user_id:
            self.queryset = TaskModel.objects.filter(user_id=user_id)

        serializer = TaskSerializer(self.queryset, many=True)
        return Response(serializer.data)

