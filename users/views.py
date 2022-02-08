from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_create.html', {'form': form})


@login_required()
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        pwd_form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        if pwd_form.is_valid():
            user = pwd_form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        pwd_form = PasswordChangeForm(request.user)

    return render(request, 'profile.html', {'form': form, 'pwd_form': pwd_form})
