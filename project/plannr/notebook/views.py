from django.shortcuts import render
from .models import DailyEntry #and other things
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
    model = DailyEntry # import that
    paginate_by = 10
    #return a context

from django.views.generic.detail import DetailView
class DailyDetailView(DetailView):
    model = DailyEntry
    #return a context
