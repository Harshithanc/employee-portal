from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TaskSerializer


class TaskListCreateAPI(ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


@login_required(login_url='/login/')
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})


@login_required(login_url='/login/')
def create_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('/tasks/')

    return render(request, 'create_task.html', {'form': form})


@login_required(login_url='/login/')
def update_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('/tasks/')

    return render(request, 'create_task.html', {'form': form})


@login_required(login_url='/login/')
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('/tasks/')