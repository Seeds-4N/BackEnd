from django.urls import path
from . import views


urlpatterns = [
    path('postcreate/', views.PostListView.as_view()),
    path('postlist/', views.PostListView.as_view()),

]