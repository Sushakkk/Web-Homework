from django.contrib import admin
from .models import BugReport, FeatureRequest

# Регистрация модели BugReport в административной панели
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    # Определение отображаемых полей в списке объектов BugReport
    list_display = ('title', 'status', 'project', 'task', 'created_at', 'updated_at')
    # Добавление фильтров для быстрого поиска BugReport по статусу, проекту и задаче
    list_filter = ('status', 'project', 'task')
    # Добавление поисковой строки для быстрого поиска BugReport по заголовку и описанию
    search_fields = ('title', 'description')
    # Определение групп полей для формы редактирования BugReport
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status', 'project', 'task')  # Определение основных полей
        }),
        ('Dates', {
            'fields': ('created_at',),  # Добавление поля даты создания
            'classes': ('collapse',),   # Добавление collapse, чтобы скрыть по умолчанию
        }),
    )
    # Определение полей только для чтения (created_at и updated_at)
    readonly_fields = ('created_at', 'updated_at')

    # Определение пользовательского действия для изменения статуса выбранных отчетов
    actions = ['change_status_to_resolved']

    # Функция для пользовательского действия
    def change_status_to_resolved(self, request, queryset):
        queryset.update(status='Completed')

    # Определение названия пользовательского действия
    change_status_to_resolved.short_description = "Mark selected bug reports as resolved"

# Регистрация модели FeatureRequest в административной панели
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    # Определение отображаемых полей в списке объектов FeatureRequest
    list_display = ('title', 'status', 'project', 'task', 'created_at', 'updated_at')
    # Добавление фильтров для быстрого поиска FeatureRequest по статусу, проекту и задаче
    list_filter = ('status', 'project', 'task')
    # Добавление поисковой строки для быстрого поиска FeatureRequest по заголовку и описанию
    search_fields = ('title', 'description')
    # Определение групп полей для формы редактирования FeatureRequest
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status', 'project', 'task')  # Определение основных полей
        }),
        ('Dates', {
            'fields': ('created_at',),  # Добавление поля даты создания
            'classes': ('collapse',),   # Добавление collapse, чтобы скрыть по умолчанию
        }),
    )
    # Определение полей только для чтения (created_at и updated_at)
    readonly_fields = ('created_at', 'updated_at')
