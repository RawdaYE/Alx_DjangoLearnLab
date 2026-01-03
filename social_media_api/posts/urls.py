from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed, like_post, unlike_post
from django.urls import path


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls
urlpatterns += [
    path('feed/', feed, name='feed'),
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),
]
