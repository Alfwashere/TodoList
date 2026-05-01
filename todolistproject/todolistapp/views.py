from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect

# Create your views here.

def index(request):
    task=Task.objects.all()
    if request.method=='POST':
        a= request.POST.get('item')
        b= request.POST.get('description')
        c=request.POST.get('priority')
        Task.objects.create(name=a, description=b, priority=c)
        return redirect('index')
    return render(request, 'index.html',{'task':task})
def delete(request,id):
    Task.objects.filter(id=id).delete()
    return redirect ('index')
def edit(request,id):
    a=Task.objects.get(id=id)
    a.completed=not a.completed
    a.save()
    return redirect('index')


    