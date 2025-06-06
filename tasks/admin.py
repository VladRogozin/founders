# admin.py
from django.contrib import admin
from .models import Task, Theory
from accounts.models import Profile


class TaskInline(admin.TabularInline):  # или StackedInline
    model = Task
    extra = 0

@admin.register(Theory)
class TheoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TaskInline]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'reward')
    list_filter = ('difficulty',)
    search_fields = ('title', 'question')


from django.contrib import admin
from .models import TaskAnswer


from django.contrib import admin
from accounts.models import Profile, Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'is_accepted', 'created_at')
    list_editable = ('is_accepted',)
    search_fields = ('user__username', 'task__title', 'message')
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        profile, created = Profile.objects.get_or_create(user=obj.user)

        if not change:  # создаётся новая запись
            if obj.is_accepted:
                profile.points += obj.task.reward
                profile.coins += obj.task.reward
                profile.save()
        else:
            old_obj = Notification.objects.get(pk=obj.pk)
            if obj.is_accepted and not old_obj.is_accepted:
                profile.points += obj.task.reward
                profile.coins += obj.task.reward
                profile.save()
            elif not obj.is_accepted and old_obj.is_accepted:
                # обратное списание, если нужно
                pass

        super().save_model(request, obj, form, change)


@admin.register(TaskAnswer)
class TaskAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'is_accepted', 'created_at')
    list_editable = ('is_accepted',)
    readonly_fields = ('user', 'task', 'user_answer', 'created_at')

    def save_model(self, request, obj, form, change):
        if change:
            old_obj = TaskAnswer.objects.get(pk=obj.pk)
            if obj.is_accepted and not old_obj.is_accepted:
                profile, created = Profile.objects.get_or_create(user=obj.user)
                profile.points += obj.task.reward
                profile.coins += obj.task.reward  # 💡 ВОТ ЭТО ДОБАВЬ
                profile.save()
        super().save_model(request, obj, form, change)

admin.site.register(Profile)


