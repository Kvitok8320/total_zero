from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Аутентификация и вход пользователя
            user = authenticate(email=user.email, password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('create_order')  # Замените 'create_order' на имя вашей целевой страницы
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})

def registration_success(request):
    return render(request, 'register/registration_success.html')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create_order')  # Перенаправляем пользователя на целевую страницу после успешного входа
    else:
        form = UserLoginForm()
    return render(request, 'register/login.html', {'form': form})