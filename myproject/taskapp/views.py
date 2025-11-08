from rest_framework import viewsets, permissions
from .models import Task
from rest_framework import serializers
from .serializers import TaskSerializer


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Task
from .forms import TaskForm, StatusRemarksForm
from django.contrib.auth import get_user_model



# from rest_framework.permissions import AllowAny

# class TaskViewSet(viewsets.ModelViewSet):
#     permission_classes = [AllowAny]
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer



@login_required
def dashboard(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assignee=request.user)
    return render(request, 'taskapp/dashboard.html', {'tasks': tasks})

def task_tracking(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assignee=request.user)
    return render(request, 'taskapp/task_tracking.html', {'tasks': tasks})

# your_app/views.py

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # adjust for your needs


@login_required
def task_list(request):
    # Filter tasks assigned only to the current user if not admin
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assignee=request.user)
    
    context = {
        'tasks': tasks,
    }
    return render(request, 'taskapp/task_list.html', context)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskapp/task_detail.html', {'task': task})

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskapp:task_list')
        task = form.instance  # So selections persist on form error
    else:
        form = TaskForm()
        task = None

    users = User.objects.all()  # Or use a filter as desired

    return render(
        request,
        'taskapp/task_form.html',
        {
            'form': form,
            'users': users,
            'task': task,  # For selections in your template
        }
    )

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    # Only allow admin or task assignee:
    if not (request.user.is_superuser or task.assignee == request.user):
        return HttpResponseForbidden("You are not allowed to update this task.")
    
    if request.method == "POST":
        # Conditional form instantiation for POST
        if request.user.is_superuser:
            form = TaskForm(request.POST, instance=task)
        else:
            form = StatusRemarksForm(request.POST, instance=task)
        if form.is_valid():
            # Additional field restrictions for non-admins can go here
            form.save()
            return redirect('taskapp:task_list')
    else:
        # Conditional form instantiation for GET (initial load)
        if request.user.is_superuser:
            form = TaskForm(instance=task)
        else:
            form = StatusRemarksForm(instance=task)
    
    # You may need this in context for your template (for admin only)
    users = User.objects.all() if request.user.is_superuser else None

    context = {
        "form": form,
        "users": users,
        "task": task,
    }
    return render(request, "taskapp/task_form.html", context)


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # Only admin can delete
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to delete this task.")
    
    if request.method == 'POST':
        task.delete()
        return redirect('taskapp:task_list')
    return render(request, 'taskapp/confirm_delete.html', {'task': task})




def timeline_view(request):
    tasks = Task.objects.order_by('start_date')
    return render(request, 'taskapp/timeline.html', {'tasks': tasks})