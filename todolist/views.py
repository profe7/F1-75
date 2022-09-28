import datetime
from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from todolist.forms import Todo, updateTodo
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/todolist/login/')
def render_todolist(request):
    data = Task.objects.filter(user=request.user)
    context = {
        'tasks':data
    }
    return render(request, 'todolist.html', context)


def render_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:render_todolist"))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def render_logout(request):
    messages.success(request, 'Anda berhasil logout!')
    logout(request)
    return redirect('todolist:render_login')


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:render_login')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)


@login_required(login_url='/todolist/login/')
def render_create(request):
    if request.method == 'POST':
        todo = Todo(request.POST)
        if todo.is_valid():
            todosave = Task(
                user = request.user,
                date = datetime.datetime.now(),
                title = todo.cleaned_data['nama'],
                description = todo.cleaned_data['deskripsi']
            )
            todosave.save()
            messages.success(request, 'Todo berhasil dibuat!')
            return redirect('todolist:render_todolist')
    todo = Todo()
    context = {
        'form':todo
    }
    return render(request, 'create.html', context)


@login_required(login_url='/todolist/login/')
def render_delete(request, id):
    qs = Task.objects.get(id=id)
    if request.method == 'POST':
        qs.delete()
        return redirect('todolist:render_todolist')
    context = {
        'todo': qs
    }
    return render(request, 'delete.html', context)
# Create your views here.


@login_required(login_url='/todolist/login/')
def render_update(request, id):
    qs = Task.objects.get(id=id)
    todo = updateTodo(instance=qs)
    if request.method == 'POST':
        todo = updateTodo(request.POST, instance=qs)
        if todo.is_valid():
            todo.save()
            return redirect('todolist:render_todolist')
    context = {
        'todo':todo
    }
    return render(request, 'update.html', context)