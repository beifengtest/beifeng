from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'base.html',locals())

def getTodo(request,todoid):
    print todoid
    return render(request,'base.html',locals())
