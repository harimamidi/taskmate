from django import forms
from todolist_app.models import taskList

class taskForm(forms.ModelForm):
    class Meta:
        model = taskList
        fields = ['task', 'done']