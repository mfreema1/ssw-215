from django.shortcuts import render
from .models import DailyEntry, Task, LookingForwardTo, ThankfulFor 
from .models import WeeklyEntry, Project, WeeklyGoal
from django.contrib.auth.decorators import login_required # allow auth checking for function based views
from django.contrib.auth.mixins import LoginRequiredMixin # allow auth checking for class based views


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    """
    Return our example index page to show templating
    """
    return render (
        request,
        'index.html',
        context = {}
    )

# empty context because nothing in our template actually
# needs to be filled

# add our mixin to enforce logging in for our users
# for our generic, class based views, we'll need to override
# our def get_queryset(self) function inside of the class
# the class based view calls this itself when it needs to grab
# the model
from django.views.generic.list import ListView
class DailyListView(LoginRequiredMixin, ListView):
    model = DailyEntry
    login_url = '/accounts/login/'
    paginate_by = 10
    def get_queryset(self):
        return DailyEntry.objects.filter(author=self.request.user)

from django.views.generic.detail import DetailView
class DailyDetailView(LoginRequiredMixin, DetailView):
    model = DailyEntry
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super(DailyDetailView, self).get_context_data(**kwargs)
        if self.object and self.request.user.is_authenticated:
            context['has_access_to_entry'] = self.object.is_viewable_by(self.request.user)
        return context
    

class WeeklyListView(LoginRequiredMixin, ListView):
    model = WeeklyEntry
    login_url = '/accounts/login/'
    paginate_by = 10
    def get_queryset(self):
        return WeeklyEntry.objects.filter(author=self.request.user)

class WeeklyDetailView(LoginRequiredMixin, DetailView):
    model = WeeklyEntry
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super(WeeklyDetailView, self).get_context_data(**kwargs)
        if self.object and self.request.user.is_authenticated:
            context['has_access_to_entry'] = self.object.is_viewable_by(self.request.user)
        return context

from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import reverse
def signup(request):
    """
    Allow for the sign up of a new user
    """
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            first_name = signup_form.cleaned_data.get('first_name')
            last_name = signup_form.cleaned_data.get('last_name')
            username = signup_form.cleaned_data.get('username')
            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password1')
            user = User.objects.create(first_name=first_name, last_name=last_name, username=username,
            email=email, password=password)
            login(request, user)
            return redirect('/notebook/')
            #save a new user model
    else:
        signup_form = SignupForm()
    return render(request, 'signup.html', context={'signup_form': signup_form})

from django.forms.formsets import formset_factory
from django.shortcuts import redirect
from .forms import DailyEntryForm, TaskForm, LookingForwardToForm, ThankfulForForm
@login_required
def add_daily_entry(request):
    """
    Allow a user to add to their daily entries
    """
    # Generate our formset classes to create instances from
    TaskFormSet = formset_factory(TaskForm)
    LookingForwardFormSet = formset_factory(LookingForwardToForm)
    ThankfulForFormSet = formset_factory(ThankfulForForm)

    #handle the response to the form
    if request.method == 'POST':

        # make our instances
        daily_entry_form = DailyEntryForm(request.POST)
        task_form_set = TaskFormSet(request.POST, prefix='tasks')
        looking_forward_form_set = LookingForwardFormSet(request.POST, prefix='looking_forward_tos')
        thankful_for_form_set = ThankfulForFormSet(request.POST, prefix='thankful_fors')

        if daily_entry_form.is_valid() and task_form_set.is_valid() and looking_forward_form_set.is_valid() and thankful_for_form_set.is_valid():
            tasks = []
            looking = []
            thankful = []
            
            #first save our entry
            author = request.user
            entry_date = daily_entry_form.cleaned_data.get('entry_date')
            affirmation = daily_entry_form.cleaned_data.get('affirmation')
            entry = DailyEntry.objects.create(author=author, entry_date=entry_date, affirmation=affirmation)
            #immediately grab the instance we just created.  Need this for foreign keys

            for task_form in task_form_set:
                title = task_form.cleaned_data.get('title')
                start_time = task_form.cleaned_data.get('start_time')
                end_time = task_form.cleaned_data.get('end_time')
                is_complete = task_form.cleaned_data.get('is_complete')
                description = task_form.cleaned_data.get('description')
                #so long as the task has a title, append it to the list of tasks
                if title:
                    tasks.append(Task(entry=entry, title=title, start_time=start_time,
                    end_time=end_time, is_complete=is_complete, description=description))

            for looking_forward_to_form  in looking_forward_form_set:
                title = looking_forward_to_form.cleaned_data.get('title')
                description = looking_forward_to_form.cleaned_data.get('description')
                if title:
                    looking.append(LookingForwardTo(entry=entry, title=title, description=description))

            for thankful_for_form in thankful_for_form_set:
                title = thankful_for_form.cleaned_data.get('title')
                description = thankful_for_form.cleaned_data.get('description')
                if title:
                    thankful.append(ThankfulFor(entry=entry, title=title, description=description))
            
            ThankfulFor.objects.bulk_create(thankful)
            LookingForwardTo.objects.bulk_create(looking)
            Task.objects.bulk_create(tasks)
            return redirect('/notebook/daily')

    else:
        daily_entry_form = DailyEntryForm()
        task_form_set = TaskFormSet(prefix='tasks')
        looking_forward_form_set = LookingForwardFormSet(prefix='looking_forward_tos')
        thankful_for_form_set = ThankfulForFormSet(prefix='thankful_fors')

    context = {
        'daily_entry_form': daily_entry_form,
        'task_form_set': task_form_set,
        'looking_forward_form_set': looking_forward_form_set,
        'thankful_for_form_set': thankful_for_form_set
    }

    return render(request, 'notebook/daily_entry_add.html', context)

from .forms import WeeklyEntryForm, ProjectForm, WeeklyGoalForm
@login_required
def add_weekly_entry(request):
    """
    Allow a user to add a weekly entry to their Plannr
    """
    # Generate our formset classes to create instances from
    ProjectFormSet = formset_factory(ProjectForm)
    WeeklyGoalFormSet = formset_factory(WeeklyGoalForm)

    if request.method == "POST":

        #generate those instances
        weekly_entry_form = WeeklyEntryForm(request.POST)
        project_form_set = ProjectFormSet(request.POST, prefix='projects')
        weekly_goal_form_set = WeeklyGoalFormSet(request.POST, prefix='goals')

        if weekly_entry_form.is_valid() and project_form_set.is_valid() and weekly_goal_form_set.is_valid():
            projects = []
            goals = []

            author = request.user
            week_start = weekly_entry_form.cleaned_data.get('week_start')
            entry = WeeklyEntry.objects.create(author=author, week_start=week_start)
            #grab that entry for later use

            for project_form in project_form_set:
                title = project_form.cleaned_data.get('title')
                description = project_form.cleaned_data.get('description')
                is_complete = project_form.cleaned_data.get('is_complete')
                if title:
                    projects.append(Project(entry=entry, title=title, description=description, 
                    is_complete=is_complete))
                
            for weekly_goal_form in weekly_goal_form_set:
                title = weekly_goal_form.cleaned_data.get('title')
                description = weekly_goal_form.cleaned_data.get('description')
                goal_type = weekly_goal_form.cleaned_data.get('goal_type')
                is_complete = weekly_goal_form.cleaned_data.get('is_complete')
                if title:
                    goals.append(WeeklyGoal(entry=entry, title=title,
                    description=description, goal_type=goal_type, is_complete=is_complete))
            
            Project.objects.bulk_create(projects)
            WeeklyGoal.objects.bulk_create(goals)
            return redirect('/notebook/weekly')

    else:
        weekly_entry_form = WeeklyEntryForm()
        project_form_set = ProjectFormSet(prefix='projects')
        weekly_goal_form_set = WeeklyGoalFormSet(prefix='goals')

    context = {
        'weekly_entry_form': weekly_entry_form,
        'project_form_set': project_form_set,
        'weekly_goal_form_set': weekly_goal_form_set
    }

    return render(request, 'notebook/weekly_entry_add.html', context)