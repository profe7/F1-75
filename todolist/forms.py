from email.policy import default
from django import forms
from todolist.models import Task

class Todo(forms.Form):
    nama = forms.CharField(label="Nama Todo", required=True)
    deskripsi = forms.CharField(label="Deskripsi Todo", required=True)
class updateTodo(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_finished']


