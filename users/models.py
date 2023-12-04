from django.db import models

class UserQuerySet(models.QuerySet):
    def for_viewset(self) -> 'UserQuerySet':
        return self.prefetch_related('tasks')


class User(models.Model):

    objects = models.Manager.from_queryset(UserQuerySet)()

    username = models.CharField(max_length=255)
