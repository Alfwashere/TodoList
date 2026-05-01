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

    