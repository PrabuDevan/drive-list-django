from django.urls import path

from . import views

urlpatterns = [
    path('first_page/', views.get_drive_files, name='get_drive_files'),
    path('next_page/', views.get_next_page, name='get_next_page'),
]
