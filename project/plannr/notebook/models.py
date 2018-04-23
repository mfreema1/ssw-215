from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
#Main tables
class DailyEntry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    entry_date = models.DateField()
    affirmation = models.TextField()

    def __str__(self):
        """
        We're going to use the date of entry to display it
        """
        return str(self.entry_date)

    def get_absolute_url(self):
        """
        Returns the url to access a detail of this entry
        """
        return reverse('daily_detail', args=[str(self.id)])

class WeeklyEntry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    week_start = models.DateField()
    week_end = models.DateField() #TODO: remove this

class MonthlyEntry(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    entry = models.ForeignKey(DailyEntry, on_delete=models.CASCADE, null=True)
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