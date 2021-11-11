from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('home/', PostListView.as_view(), name='milage-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='milage-about'),
]

