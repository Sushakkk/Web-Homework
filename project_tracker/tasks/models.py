from django.db import models
from django.contrib.auth.models import User  # Импорт модели пользователя Django

class Project(models.Model):
    name = models.CharField(max_length=100)  # Название проекта
    description = models.TextField()  # Описание проекта
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания записи
    
    def __str__(self):
        return self.name  # Возвращает название проекта в качестве его строкового представления

class Task(models.Model):
    
    # Кортеж из возможных статусов задачи
    STATUS_CHOICES = [  # Варианты статусов задачи
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    
    project = models.ForeignKey(  # Связь с моделью проекта
        Project,  # Модель проекта
        related_name='tasks',  # Имя обратной связи для доступа к связанным объектам из проекта
        on_delete=models.CASCADE  # При удалении проекта, связанные с ним задачи также удаляются
    )
    name = models.CharField(max_length=100)  # Название задачи
    description = models.TextField()  # Описание задачи
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания записи
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления записи
    assignee = models.ForeignKey(  # Связь с моделью пользователя (исполнитель задачи)
        User,  # Модель пользователя Django
        related_name='tasks',  # Имя обратной связи для доступа к связанным объектам из пользователя
        on_delete=models.SET_NULL,  # При удалении пользователя, связанный с ним задачи устанавливаются в NULL
        null=True,  # Разрешение значения NULL для поля assignee
        blank=True  # Разрешение оставить поле пустым в административном интерфейсе
    )
    
    # Новое поле статуса задачи
    status = models.CharField(  # Поле статуса задачи
        max_length=50,  # Максимальная длина поля
        choices=STATUS_CHOICES,  # Возможные значения поля
        default='New',  # Значение по умолчанию
    )
