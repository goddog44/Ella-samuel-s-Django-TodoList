# Import required Django modules and project-specific models and forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Task, Tag, User
from .forms import TaskForm, TagForm, RegistrationForm, LoginForm

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create the user directly using form data, properly handling the password
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect("login")
        else:
            return render(request, "register.html", {"form": form})
    else:
        return render(request, "register.html", {"form": RegistrationForm()})
    
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if user is not None and user.is_active:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "login.html", {"form": form, "error": "Invalid login"})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Task Management Views
@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    tags = Tag.objects.all()
    return render(request, 'home.html', {'tasks': tasks, 'user': request.user, 'tags': tags})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.delete()
    return redirect('home')

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.status = 'completed' if task.status == 'incomplete' else 'incomplete'
    task.save()
    return redirect('home')

# Tag Management Views
@login_required
def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TagForm()
    return render(request, 'create_tag.html', {'form': form})

@login_required
def add_tag_to_task(request, task_id, tag_name):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    tag = get_object_or_404(Tag, pk=tag_name)
    task.tags.add(tag)
    return redirect('home')

@login_required
def remove_tag_from_task(request, task_id, tag_name):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    tag = get_object_or_404(Tag, pk=tag_name)
    task.tags.remove(tag)
    return redirect('home')