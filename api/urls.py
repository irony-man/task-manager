from django.urls import path, include
from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', ArticleViewSet, basename='tasks')
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('article/<int:id>', ArticleDetail.as_view())
]
