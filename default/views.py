from django.shortcuts import render
from .models import Poll
from django.views.generic import ListView

# Create your views here.
def Poll_list(req):
    polls-Poll.objects.all()
    return render(req,"poll_list.html",{"poll_list":polls})
    

class Poll_list(ListView):
    model=Poll

