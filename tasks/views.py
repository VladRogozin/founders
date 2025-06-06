from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
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
                # Перенаправление на ту же задачу
                url = reverse('task_list') + f'?task_id={selected_task.id}'
                return HttpResponseRedirect(url)
        else:
            form = TaskAnswerForm()

    # Получаем связанную теорию, если есть
    related_theory = selected_task.theory if selected_task and selected_task.theory else None

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'selected_task': selected_task,
        'form': form,
        'related_theory': related_theory,
    })
