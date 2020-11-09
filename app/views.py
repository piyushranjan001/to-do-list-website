from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    # return HttpResponse("This is todolist")
    all_to_do_items = TodoItem.objects.all()
    return render(request,'basic.html',{'all_items':all_to_do_items})

def addTodo(request):
    # create a new to do item
    # save it
    # rediret to browser /todo/
    # c = request.POST['content']
    # new_item = TodoItem(content=c)
    new_item = TodoItem(content= request.POST["content"])
    new_item.save()
    return HttpResponseRedirect('/app/')

def deleteTodo(request,todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/app/')