from django.urls import path
from folders import views


urlpatterns = [
    path('folders/', views.get_folders, name='get_folders'),
    path('folders/create/', views.create_folder, name='create_folder'),
    path('folders/add_location/', views.add_location_to_folder, name='add_location_to_folder'),
    path('folders/<int:folder_id>/locations/', views.folder_locations, name='folder_locations'),    # 특정 폴더의 장소 목록 조회
]
