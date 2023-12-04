from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.models import Tasks
from tasks.views.serializers import TodoSerializer, TodoShortSerializer
from users.models import User


class TodoViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        queryset = Tasks.objects.filter(user=user_param)
        serializer = TodoShortSerializer(queryset, many=True)

