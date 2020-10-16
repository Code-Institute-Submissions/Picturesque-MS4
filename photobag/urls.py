from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_photobag, name='view_photobag'),
    path('add/<item_id>/', views.add_to_photobag, name='add_to_photobag'),
]