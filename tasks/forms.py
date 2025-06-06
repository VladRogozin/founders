from django import forms
from .models import TaskAnswer

class TaskAnswerForm(forms.ModelForm):
    class Meta:
        model = TaskAnswer
        fields = ['user_answer']
        widgets = {
            'user_answer': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Введите ваш ответ...'}),
        }
        labels = {
            'user_answer': 'Ваш ответ:',
        }
