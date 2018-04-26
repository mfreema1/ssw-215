from django.shortcuts import render
from .models import DailyEntry, Task, WeeklyEntry #and other things
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
    #order this by date
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
        context['user_from_req'] = self.request.user
        context['user_from_mod'] = self.object.getUser()
        return context
    

class WeeklyListView(LoginRequiredMixin, ListView):
    model = WeeklyEntry
    login_url = '/accounts/login/'
    #order this somehow
    paginate_by = 10

class WeeklyDetailView(LoginRequiredMixin, DetailView):
    model = WeeklyEntry
    login_url = '/accounts/login/'
    """
    Shouldn't need to run any kind of pre-processing here.  We can just grab all of our
    foreign keys from directly inside of the template
    """