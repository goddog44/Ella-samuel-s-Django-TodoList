from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Default route to the home view
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_task/', views.create_task, name='create_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('create_tag/', views.create_tag, name='create_tag'),
    path('add_tag/<int:task_id>/<str:tag_name>/', views.add_tag_to_task, name='add_tag'),
    path('remove_tag/<int:task_id>str:tag_name>/', views.remove_tag_from_task, name='remove_tag'),
]