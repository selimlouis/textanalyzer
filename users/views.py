from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from analyze.models import Report


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! You are now able to log in')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'title': 'Register', 'form': form})


#handle requirements with built in decorator
@login_required
def profile(request):
    reports = request.user.report_set.all()
    return render(request, 'users/profile.html', {'title': 'Profile', 'reports': reports})