from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import TaskForm

# 할 일 목록
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, completed=False)
            return redirect('task_list')
        else:
            # 제목이 비었을 경우의 처리 (예: 에러 메시지 반환)
            return render(request, 'todo/task_list.html', {
                'error': '제목을 입력해주세요.'  # 제목이 없을 경우 오류 메시지 표시
            })

    # 완료되지 않은 작업들
    tasks = Task.objects.filter(completed=False)
    # 완료된 작업들
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'todo/task_list.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })

# 작업 완료 상태를 반전시키는 뷰
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # 완료 상태 반전
    task.save()
    return redirect('task_list')

# 작업 삭제하는 뷰
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')