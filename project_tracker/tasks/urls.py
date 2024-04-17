from django.urls import path, include  # Импорт функции include из модуля django.urls

# Ваши другие импорты и код здесь

from tasks import views  # Импорт модуля views из приложения tasks

app_name = 'tasks'  # Определение пространства имен для приложения tasks

urlpatterns = [
    path('', views.index),  # Определение URL-шаблона для пустого пути и связывание с представлением index из модуля views
    path('another/', views.another_page, name='another_page'),  # новый маршрут
    path('quality_control/', include('quality_control.urls')),  # Включение маршрутов из приложения quality_control
]
