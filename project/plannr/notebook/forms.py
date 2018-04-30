from django.forms import ModelForm
from django.forms import Form
from notebook.models import DailyEntry, Task, LookingForwardTo, ThankfulFor

class DailyEntryForm(ModelForm):
    class Meta:
        model = DailyEntry
        fields = ['entry_date', 'affirmation']

    def __init__(self, *args, **kwargs):
        super(DailyEntryForm, self).__init__(*args, **kwargs)
        self.fields['entry_date'].widget.attrs.update({'class':'form-control'})
        self.fields['affirmation'].widget.attrs.update({'class':'form-control'})


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'start_time', 'end_time', 'description', 'is_complete']
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['start_time'].widget.attrs.update({'class':'form-control'})
        self.fields['end_time'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})

class LookingForwardToForm(ModelForm):
    class Meta:
        model = LookingForwardTo
        fields = ['title', 'description']
    
    def __init__(self, *args, **kwargs):
        super(LookingForwardToForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})

class ThankfulForForm(ModelForm):
    class Meta:
        model = ThankfulFor
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(ThankfulForForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})

#this is the start of the new user signup form.  We don't need to
#add anything to the __init__ method of this, mainly because it's
#a static form that does not change its number of inputs.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length = 32, required=False)
    last_name = forms.CharField(max_length = 32, required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

from notebook.models import WeeklyEntry, Project, WeeklyGoal
class WeeklyEntryForm(ModelForm):
    class Meta:
        model = WeeklyEntry
        fields = ['week_start']

    def __init__(self, *args, **kwargs):
        super(WeeklyEntryForm, self).__init__(*args, **kwargs)
        self.fields['week_start'].widget.attrs.update({'class':'form-control'})

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'is_complete']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        #self.fields['is_complete'].widget.attrs.update({'class':'form-control'})

class WeeklyGoalForm(ModelForm):
    class Meta:
        model = WeeklyGoal
        fields = ['title', 'description', 'goal_type', 'is_complete']

    def __init__(self, *args, **kwargs):
        super(WeeklyGoalForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['goal_type'].widget.attrs.update({'class':'form-control'})
        #self.fields['is_complete'].widget.attrs.update({'class':'form-control'})