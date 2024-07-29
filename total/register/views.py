from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
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
            return redirect('order/create_order.html')  # Замените 'home' на имя вашей целевой страницы
    else:
        form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})

    #return render(request, 'register/register.html', {'form': form})


def registration_success(request):
    return render(request, 'register/registration_success.html')