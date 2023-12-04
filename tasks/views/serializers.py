from rest_framework.fields import IntegerField, CharField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from tasks.models import Tasks
from users.models import User


class TodoSerializer(ModelSerializer):

    id = IntegerField(read_only=True)
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    description = CharField(allow_null=True, required=False)

    class Meta:
        model = Tasks
        fields = [
            'id',
            'title',
            'description',
            'user',
            'is_completed'
        ]


class TodoShortSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    description = CharField(allow_null=True, required=False)

    class Meta:
        model = Tasks
        fields = [
            'id',
            'title',
            'description',
            'is_completed'
        ]
