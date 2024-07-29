from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()

    return render(request, 'register/register.html', {'form': form})


def registration_success(request):
    return render(request, 'register/registration_success.html')