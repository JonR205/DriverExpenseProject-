from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='milage-home'),
    path('about/', views.about, name='milage-about'),
]