from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'start_date', 'due_date', 'status', 'remarks']

class StatusRemarksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status', 'remarks']
