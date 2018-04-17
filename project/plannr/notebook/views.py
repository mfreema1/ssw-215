from django.shortcuts import render

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