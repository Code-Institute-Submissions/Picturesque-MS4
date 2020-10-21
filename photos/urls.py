from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_photos, name='photos'),
    path('<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('add/', views.add_photo, name='add_photo'),
]
