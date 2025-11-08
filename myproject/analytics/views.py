from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from taskapp.models import Task

@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to access this page.")
    
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='completed').count()
    in_progress = Task.objects.filter(status='progress').count()  # Adjust if using 'in_progress' or similar
    to_do = total_tasks - completed_tasks - in_progress

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'in_progress': in_progress,
        'to_do': to_do,
    }
    return render(request, 'analytics/dashboard.html', context)
