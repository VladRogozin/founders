from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
from .forms import TaskAnswerForm


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Task, TaskAnswer
from .forms import TaskAnswerForm

@login_required
def task_list(request):
    tasks = Task.objects.all()
    selected_task_id = request.GET.get('task_id')
    selected_task = get_object_or_404(Task, id=selected_task_id) if selected_task_id else None

    form = None
    if selected_task:
        if request.method == 'POST':
            form = TaskAnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.user = request.user
                answer.task = selected_task
                answer.save()
                url = reverse('task_list') + f'?task_id={selected_task.id}'
                return HttpResponseRedirect(url)
        else:
            form = TaskAnswerForm()

    # Получаем список id заданий, которые пользователь уже выполнил (с подтверждённым ответом)
    completed_task_ids = TaskAnswer.objects.filter(
        user=request.user,
        is_accepted=True
    ).values_list('task_id', flat=True).distinct()

    # Связанная теория для выбранного задания
    related_theory = selected_task.theory if selected_task and selected_task.theory else None

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'selected_task': selected_task,
        'form': form,
        'related_theory': related_theory,
        'completed_task_ids': completed_task_ids,
    })


def pentagon(request):
    return render(request, 'tasks/pentagon_page.html')

