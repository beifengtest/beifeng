from django.shortcuts import render
from todo.forms import DreamForm
from todo.models import Dream

# Create your views here.

def index(request):
    dreamForm = DreamForm({'content':''})
    dreamList = Dream.objects.all()

    # return render(request,'base.html',locals())
    return render(request,'index.html',locals())