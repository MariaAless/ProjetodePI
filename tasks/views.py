from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def index(request):
   #oque pegar do banco de dados
        tasks_list = Task.objects.all().order_by('-created_at') #to peganto todo os objetos de task do banco e pegando do mais novo para o mais antigo
        paginator = Paginator(tasks_list, 3)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

         
        return render(request, "tasks/index.html",{'tasks': tasks})

def taskList(request):
   
        #oque pegar do banco de dados
        tasks_list = Task.objects.all().order_by('-created_at') #to peganto todo os objetos de task do banco e pegando do mais novo para o mais antigo
        paginator = Paginator(tasks_list, 3)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

         
        return render(request, "tasks/list.html",{'tasks': tasks})
       

def yourName(request,name):
    return render(request, "tasks/yourname.html",{'name': name})

def taskView(request,id):
    task = get_object_or_404(Task, pk=id) #tenta pegar um registro no banco e se não tiver retonar o erro 404,arumentos(model,o id é a referencia da chave primaria)
    return render(request,"tasks/task.html",{'task':task}) 

def newTask(request):
    if request.method ==  'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            form = TaskForm()
    else:
        form = TaskForm() #definir uma variavel camndo o formulario
        return render(request,'tasks/addtask.html', {'form': form})

    return render(request, 'tasks/addtask.html', {'form': form})
        
def editTask(request, id):
    task=get_object_or_404(Task,pk=id)
    form=TaskForm(instance=task)
     

    if(request.method == "POST"):
        form =TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            messages.info(request, 'Tarefa editada com sucesso!')
            return redirect('task-list') #retorna a lista
            
        else:
             return render (request, 'tasks/edittask.html', {'form': form, 'task': task})

    else:
        return render (request, 'tasks/edittask.html', {'form': form, 'task': task})

def deleteTask(request, id):
    task=get_object_or_404(Task,pk=id)
    
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('task-list')



