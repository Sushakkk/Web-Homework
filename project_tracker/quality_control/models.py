from django.db import models
from tasks.models import Project, Task


# Create your models here.

class BugReport(models.Model):
    STATUS_CHOICES = [('Новая', 'New'), ('В работе', 'In work'), ('Завершена', 'Finished'),]
    PRIORITY_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='BugReport', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='BugReport', on_delete=models.SET_NULL, null=True, blank=True )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Новая')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [('Рассмотрение','Рассмотрение'), ('Принято', 'Принято'), ('Отклонено', 'Отклонено')]
    PRIORITY_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='FeatureRequest', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='FeatureRequest', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Рассмотрение')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

