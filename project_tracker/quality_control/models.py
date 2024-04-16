from django.db import models
from tasks.models import Project, Task  # Импорт моделей проекта и задачи

class BugReport(models.Model):
    title = models.CharField(max_length=100)  # Краткое описание бага
    description = models.TextField()  # Полное описание бага
    project = models.ForeignKey(  # Связь с моделью проекта
        Project,  # Модель проекта
        related_name='bug_reports',  # Имя обратной связи для доступа к связанным объектам из проекта
        on_delete=models.CASCADE  # При удалении проекта, связанные с ним баги также удаляются
    )
    task = models.ForeignKey(  # Связь с моделью задачи
        Task,  # Модель задачи
        related_name='bug_reports',  # Имя обратной связи для доступа к связанным объектам из задачи
        on_delete=models.SET_NULL,  # При удалении задачи, связанный с ней баг устанавливается в NULL
        null=True,  # Разрешение значения NULL для поля task
        blank=True  # Разрешение оставить поле пустым в административном интерфейсе
    )
    STATUS_CHOICES = [  # Варианты статусов бага
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    status = models.CharField(  # Поле статуса бага
        max_length=50,  # Максимальная длина поля
        choices=STATUS_CHOICES,  # Возможные значения поля
        default='New',  # Значение по умолчанию
    )
    priority = models.IntegerField(default=1)  # Приоритет бага (пятибалльная шкала)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания записи
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления записи

class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)  # Название запроса на новую функцию
    description = models.TextField()  # Описание запроса
    project = models.ForeignKey(  # Связь с моделью проекта
        Project,  # Модель проекта
        related_name='feature_requests',  # Имя обратной связи для доступа к связанным объектам из проекта
        on_delete=models.CASCADE  # При удалении проекта, связанные с ним запросы на функции также удаляются
    )
    task = models.ForeignKey(  # Связь с моделью задачи
        Task,  # Модель задачи
        related_name='feature_requests',  # Имя обратной связи для доступа к связанным объектам из задачи
        on_delete=models.SET_NULL,  # При удалении задачи, связанный с ней запрос на функцию устанавливается в NULL
        null=True,  # Разрешение значения NULL для поля task
        blank=True  # Разрешение оставить поле пустым в административном интерфейсе
    )
    STATUS_CHOICES = [  # Варианты статусов запроса на функцию
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    status = models.CharField(  # Поле статуса запроса на функцию
        max_length=50,  # Максимальная длина поля
        choices=STATUS_CHOICES,  # Возможные значения поля
        default='Consideration',  # Значение по умолчанию
    )
    priority = models.IntegerField(default=1)  # Приоритет запроса на функцию (пятибалльная шкала)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания запроса
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления запроса
