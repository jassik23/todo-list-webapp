from rest_framework.routers import SimpleRouter
from tasks.views.viewsets import TodoViewSet

router = SimpleRouter()

router.register('todos', TodoViewSet)

urlpatterns = router.urls
