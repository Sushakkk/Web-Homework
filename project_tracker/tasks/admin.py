from django.contrib import admin
from .models import Project, Task


# Inline класс для модели Task
class TaskInline(admin.TabularInline):
    model = Task
    extra = 0 # Не отображать пустые формы для новых задач по умолчанию
    # Определение полей для редактирования задач
    fields = ('name', 'description', 'assignee', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at') # Поля только для чтения
    can_delete = True # Разрешение удаления задач
    show_change_link = True # Добавление ссылки для перехода к форме редактирования задачи
    
# Регистрация модели Project в административном интерфейсе
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Определение отображаемых полей в списке объектов проектов
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')# Добавление поисковой строки для быстрого поиска проектов
    ordering = ('created_at',)# Определение порядка сортировки проектов по дате создания
    date_hierarchy = 'created_at'# Добавление навигации по датам для удобства поиска проектов
    
     # Подключение inline для Task
    inlines = [TaskInline]
    
# Регистрация модели Task в административном интерфейсе
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Определение отображаемых полей в списке объектов задач
    list_display = ('name', 'project', 'assignee', 'status', 'created_at', 'updated_at')
    
    list_filter = ('status', 'assignee', 'project') # Добавление фильтров для быстрого поиска задач по статусу, назначенному пользователю и проекту
    
    search_fields = ('name', 'description')# Добавление поисковой строки для быстрого поиска задач
    
    list_editable = ('status', 'assignee')# Позволяет редактировать статус и назначенного пользователя непосредственно в списке задач
    
    readonly_fields = ('created_at', 'updated_at')# Определение полей только для чтения, таких как дата создания и обновления
