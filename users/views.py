from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from tasks.models import Task
from django.contrib.auth.decorators import login_required

#register view
def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/dashboard/')

    return render(request, 'register.html', {'form': form})



#login view
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/dashboard/')

    return render(request, 'login.html')

#create dashboard

@login_required(login_url='/login/')
def dashboard(request):
    total_tasks = Task.objects.filter(user=request.user).count()
    pending_tasks = Task.objects.filter(user=request.user, status='Pending').count()
    completed_tasks = Task.objects.filter(user=request.user, status='Completed').count()

    context = {
        'total_tasks': total_tasks,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'dashboard.html', context)

#logout view

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('/login/')