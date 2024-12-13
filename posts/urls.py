from django.urls import path
from . import views
from .api_views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/update/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/like/', views.post_like, name='post_like'),
    path('api/posts/', PostListAPIView.as_view(), name='api_post_list'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='api_post_detail'),
    path('post/<int:pk>/delete/', views.post_confirm_delete, name='post_confirm_delete'),
]