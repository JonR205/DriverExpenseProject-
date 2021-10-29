from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='milage-home'),
    path('about/', views.about, name='milage-about'),
]