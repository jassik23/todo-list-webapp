from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.models import Todo
from tasks.views.serializers import TodoShortSerializer
from users.models import User
from users.views.serializers import UserSerializer, UserListSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.for_viewset()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        try:
            qs = self.get_queryset()
            return Response(data=UserListSerializer(qs, many=True).data)
        except:
            return Response({'error': 'Где-то был косяк', 'status': status.HTTP_418_IM_A_TEAPOT}, status=status.HTTP_418_IM_A_TEAPOT)


    @action(detail=True, methods=['get'])
    def tasks(self, *args, **kwargs):
        user = self.get_object()
        return Response(data=TodoShortSerializer(Todo.objects.filter(user=user), many=True).data)



