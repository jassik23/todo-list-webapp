from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from tasks.views.serializers import  TodoShortSerializer
from users.models import User


class UserSerializer(ModelSerializer):

    id = IntegerField(read_only=True)
    tasks = TodoShortSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'tasks',
        ]


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',

        ]