from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('tasks/', views.index),
    path('tasks/projects/', views.projects_list, name='projects_list'),
    path('tasks/projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('tasks/projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/feedback/', views.feedback_view, name='feedback'),
    path('tasks/project/new/', views.project_create, name="project_create"),
    path('tasks/project/<int:project_id>/add_task/', views.add_task_to_project, name='add_task_to_project'),
    # ----------------------------------------CBV-------------------------------------------------------
    # path('tasks/project/create/', views.ProjectCreateView.as_view(), name='create_project'),
    # path('tasks/project/<int:project_id>/add_task/', views.TaskCreateView.as_view(), name='add_task_to_project'),
    path('tasks/project/<int:project_id>/update/', views.update_project, name='update_project'),
    path('tasks/project/<int:project_id>/task/<int:task_id>/update/', views.update_task, name='update_task'),
    # ----------------------------------------CBV-------------------------------------------------------
    # path('tasks/project/<int:project_id>/update/', views.ProjectUpdateView.as_view(), name='update_project'),
    # path('tasks/project/<int:project_id>/tasks/<int:task_id>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('tasks/project/<int:project_id>/delete', views.delete_project, name="delete_project"),
    path('tasks/project/<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]
