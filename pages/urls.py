from django.urls import path
from .views import PostListView, PostDetailView, PostDeleteView, PostUpdateView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
]
