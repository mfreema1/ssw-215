from django.contrib import admin

# import models
from .models import DailyEntry, WeeklyEntry, MonthlyEntry, Task

@admin.register(DailyEntry)
class DailyEntryAdmin(admin.ModelAdmin):
    list_display = ('entry_date', 'affirmation')

@admin.register(WeeklyEntry)
class WeeklyEntryAdmin(admin.ModelAdmin):
    list_display = ('week_start', 'week_end')

@admin.register(MonthlyEntry)
class MonthlyEntryAdmin(admin.ModelAdmin):
    list_display = ('habit', 'focus', 'month')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'description', 'is_complete')