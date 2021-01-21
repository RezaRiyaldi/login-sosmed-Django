from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from social_django.models import UserSocialAuth
# Create your views here.

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider = 'github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        google_login = user.social_auth.get(provider = 'google')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    try:
        facebook_login = user.social_auth.get(provider = 'facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    

    return render(request, 'core/settings.html', {
        'github_login':github_login,
        'google_login':google_login,
        'facebook_login':facebook_login,
        'can_disconnect':can_disconnect
        
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password kamu berhasil diupdate!')
            return redirect('password')
        else:
            messages.error(request, 'Harap perbaiki kesalahan')
    
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form':form})