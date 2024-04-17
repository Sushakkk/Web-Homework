from django.urls import path
from . import views

app_name = 'quality_control'  # Пространство имен для приложения quality_control

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница системы контроля качества
    path('bugs/', views.bug_list, name='bugs'),  # Список отчетов об ошибках
    path('features/', views.feature_list, name='features'),  # Список запросов на улучшение
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),  # Детали конкретного бага
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),  # Детали конкретного улучшения
]
