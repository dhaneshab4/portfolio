from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Portfolio
from .forms import ProjectForm, EducationForm

@login_required
def portfolio_list(request):
    portfolio = Portfolio.objects.all()
    context = {'portfolio_list': portfolio}
    return render(request, "portfolio_list.html", context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to your login page

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = EducationForm()
    return render(request, 'add_education.html', {'form': form})


