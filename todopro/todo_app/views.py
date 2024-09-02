from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import TodoForm
from .models import TodoTask

# Create your views here.



class TodoListView(ListView):
    model=TodoTask
    template_name = 'home.html'
    context_object_name = 'task1'

class TodoDetailView(DetailView):
    model = TodoTask
    template_name = 'detail.html'
    context_object_name = 'task'


class TodoUpdateView(UpdateView):
    model = TodoTask
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TodoDeleteView(DeleteView):
    model = TodoTask
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')








def home(requset):
    task1 = TodoTask.objects.all()
    if  requset.method=='POST':
        name=requset.POST.get('task','')
        priority=requset.POST.get('priority','')
        date=requset.POST.get('date','')
        task=TodoTask(name=name,priority=priority,date=date)
        task.save()
    return render(requset,'home.html',{'task1':task1})


def delete(request,todotaskid):
    task=TodoTask.objects.get(id=todotaskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')






def update(request,id):
    task=TodoTask.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=task)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})


















