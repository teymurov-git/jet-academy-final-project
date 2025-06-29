from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as django_login

# Create your views here.

def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST) 
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if not user:
                messages.error(request, 'Enter your valid information!')
                return redirect('signin')
            else:
                django_login(request, user)
                return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'signin.html', context)

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Bu vacibdir
        user.save()
        messages.success(request, 'Signup process is completed!')
        return redirect('signup')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)