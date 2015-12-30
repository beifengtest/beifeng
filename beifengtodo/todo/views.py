from django.shortcuts import render
from todo.forms import TodoForm
from todo.models import Todo
# Create your views here.

def index(request):
    todoForm = TodoForm({'content':''})
    todolist = Todo.objects.all()

    return render(request,'index.html',locals())

    # return render(request,'base.html',locals())