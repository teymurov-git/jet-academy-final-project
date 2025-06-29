from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from account.forms import RegisterForm

# Create your views here.

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup process is completed!')
            return redirect(reverse_lazy('signup'))
        else:
            messages.error(request, 'Formda xətalar var. Zəhmət olmasa yoxlayın.')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)