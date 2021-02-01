
from django import forms

from todos.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title',)


class CompleteToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('is_completed',)
