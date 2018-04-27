from django.forms import ModelForm
from django.forms import Form
from notebook.models import DailyEntry, Task, LookingForwardTo, ThankfulFor

class DailyEntryForm(ModelForm):
    class Meta:
        model = DailyEntry
        fields = ['entry_date', 'affirmation']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'start_time', 'end_time', 'description', 'is_complete']

class LookingForwardToForm(ModelForm):
    class Meta:
        model = LookingForwardTo
        fields = ['title', 'description']

class ThankfulForForm(ModelForm):
    class Meta:
        model = ThankfulFor
        fields = ['title', 'description']