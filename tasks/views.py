from django.shortcuts import render,redirect
from .models import Task
# Create your views here.

def index(request):
    tasks=Task.objects.filter(done=False)
    tasks_done=Task.objects.filter(done=True)
    
    context={"tasks":tasks,"tasks_done":tasks_done}
    return render(request,"index.html",context)

def add(request):
    if request.method=='POST':
        task=Task.objects.create(title=request.POST['task'])
        task.save()
        
        return redirect('tasks:index')

def done(request,task_id):
    task=Task.objects.get(id=task_id)
    if task.done== False:
        task.done=True
    else:
        task.done=False

    task.save()
    return redirect('tasks:index')

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()    
    return redirect('tasks:index')

def update(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':        
        task.title=request.POST['task']
        task.save()
        return redirect('tasks:index')
    else:
        return render(request,'update_task.html',{"task":task})
    