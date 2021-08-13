from django.shortcuts import render
from django.views.generic.detail import DetailView

from pybo.models import Todo

# Create your views here.
# def index(request, *args, **kwargs):
def index(request):
    return render(request, 'frontend/index.html')

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'frontend/index.html'