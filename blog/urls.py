from django.urls import path
from .views import (
    PostList, PostCreate, PostDetailView,
    PostUpdateView, PostDeleteView,
)

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/create/', PostCreate.as_view(), name='post-create'),
    path('posts/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<uuid:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<uuid:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]