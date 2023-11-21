from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from tasks.views.serializers import  TodoShortSerializer
from users.models import User


class UserSerializer(ModelSerializer):

    id = IntegerField(read_only=True)
    todos = TodoShortSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'todos',
        ]


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',

        ]