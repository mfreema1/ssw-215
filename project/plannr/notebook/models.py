from django.db import models
from django.contrib.auth.models import User
import uuid
#Main tables
class DailyEntry(models.Model):
    daily_entry_id = models.UUIDField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    entry_date = models.DateField()
    affirmation = models.TextField()

class WeeklyEntry(models.Model):
    weekly_entry_id = models.UUIDField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    week_start = models.DateField()
    week_end = models.DateField()

class MonthlyEntry(models.Model):
    monthly_entry_id = models.UUIDField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    habit = models.CharField(max_length=20)
    focus = models.CharField(max_length=20)
    MONTHS_IN_YEAR = (
        ('JANUARY', 'January'),
        ('FEBRUARY', 'February'),
        ('MARCH', 'March'),
        ('APRIL', 'April'),
        ('MAY', 'May'),
        ('JUNE', 'June'),
        ('JULY', 'July'),
        ('AUGUST', 'August'),
        ('SEPTEMBER', 'September'),
        ('OCTOBER', 'October'),
        ('NOVEMBER', 'November'),
        ('DECEMBER', 'December')
    )
    month = models.CharField(
        max_length=32,
        choices = MONTHS_IN_YEAR
    )

#Daily tables
class Task(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_complete = models.BooleanField()
    title = models.CharField(max_length=32)
    description = models.TextField()

class ThankfulFor(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

class LookingForwardTo(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

#Weekly tables
class Project(models.Model):
    weekly_entry_id = models.ForeignKey(
        'WeeklyEntry',
        on_delete=models.CASCADE
    )
    is_complete = models.BooleanField()
    title = models.CharField(max_length=32)
    description = models.TextField()

class WeeklyGoal(models.Model):
    GOAL_TYPES = (
        ('FAMILY', 'Family'),
        ('WORK', 'Work'),
        ('RELATIONSHIP', 'Relationship'),
        ('PERSONAL', 'Personal')
    )
    weekly_goal = models.CharField(
        max_length=32,
        choices = GOAL_TYPES
    )
    title = models.CharField(max_length=32)
    description = models.TextField()

#Monthly tables
class Obstacle(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

class Insight(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

class MonthlyGoal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    is_complete = models.BooleanField()