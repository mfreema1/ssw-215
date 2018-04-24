from django.contrib import admin

# import models
from .models import DailyEntry, WeeklyEntry, MonthlyEntry
from .models import Task, ThankfulFor, LookingForwardTo
from .models import WeeklyGoal, Project
from .models import Insight, Obstacle, MonthlyGoal

@admin.register(DailyEntry)
class DailyEntryAdmin(admin.ModelAdmin):
    list_display = ('entry_date', 'affirmation')

@admin.register(WeeklyEntry)
class WeeklyEntryAdmin(admin.ModelAdmin):
    list_display = ('week_start',) #removed week end

@admin.register(MonthlyEntry)
class MonthlyEntryAdmin(admin.ModelAdmin):
    list_display = ('habit', 'focus', 'month')

#daily entry
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'description', 'is_complete')

@admin.register(ThankfulFor)
class ThankfulForAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(LookingForwardTo)
class LookingForwardToAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

#weekly entry
@admin.register(WeeklyGoal)
class WeeklyGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'goal_type', 'is_complete')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_complete')

#monthly entry
@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Obstacle)
class ObstacleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(MonthlyGoal)
class MonthlyGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_complete')