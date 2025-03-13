from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework_nested import routers

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')

posts_router = routers.NestedSimpleRouter(router, 'posts', lookup='post')
posts_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(posts_router.urls)),
    path('v1/api-token-auth/', obtain_auth_token),
]