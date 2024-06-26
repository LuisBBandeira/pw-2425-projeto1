from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('folders/', views.folder_list, name='folder_list'),
    path('folders/<int:parent_id>/', views.folder_list, name='folder_list'),
    path('folders/create/', views.create_folder, name='create_folder'),
    path('folders/create/<int:parent_id>/', views.create_folder, name='create_folder'),
    path('folders/delete/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    path('move/<int:file_id>/', views.move_file, name='move_file'),
    path('file/delete/<int:file_id>/', views.delete_file, name='delete_file'),
]