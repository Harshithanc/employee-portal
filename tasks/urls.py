from django.urls import path
from .views import task_list, create_task, update_task, delete_task
from .views import TaskListCreateAPI, TaskDetailAPI

urlpatterns = [
    path('', task_list, name='tasks'),
    path('create/', create_task, name='create_task'),
    path('update/<int:id>/', update_task, name='update_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),

    path('api/tasks/', TaskListCreateAPI.as_view()),
    path('api/tasks/<int:pk>/', TaskDetailAPI.as_view()),
]