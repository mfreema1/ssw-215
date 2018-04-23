from django.shortcuts import render
from .models import DailyEntry, Task, WeeklyEntry #and other things
# Create your views here.
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

from django.views.generic.list import ListView
class DailyListView(ListView):
    model = DailyEntry
    paginate_by = 10

from django.views.generic.detail import DetailView
class DailyDetailView(DetailView):
    model = DailyEntry
    """
    Run some pre-processing on the data model.  Grab all of the 
    tasks for our given entry and throw them out.
    """

class WeeklyListView(ListView):
    model = WeeklyEntry
    paginate_by = 10

class WeeklyDetailView(DetailView):
    model = WeeklyEntry
    """
    Shouldn't need to run any kind of pre-processing here.  We can just grab all of our
    foreign keys from directly inside of the template
    """