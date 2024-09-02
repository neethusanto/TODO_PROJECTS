from django import forms

from .models import TodoTask


class TodoForm(forms.ModelForm):
    class Meta:
        model=TodoTask
        fields=['name','priority','date']