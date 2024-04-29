from django.contrib import admin
from .models import BugReport, FeatureRequest


# Register your models here.


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('status', 'task', 'project', 'priority')
    search_fields = ('title', 'description')
    ordering = ('created_at',)
    date_hierarchy = "created_at"


@admin.register(FeatureRequest)
class AdminFeatureRequest(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('status', 'task', 'project', 'priority')
    search_fields = ('title', 'description')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'


class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'update_at')
    readonly_fields = ('created_at', 'update_at')
    can_delete = True
    show_change_link = True


class FeatureReportInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'update_at')
    readonly_fields = ('created_at', 'update_at')
    can_delete = True
    show_change_link = True
