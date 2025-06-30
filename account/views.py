from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from account.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    next = request.GET.get('next', reverse_lazy('home'))
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
                return redirect(next)
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

def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('signin'))

@login_required
def profile(request):
    return render(request, 'profile.html')