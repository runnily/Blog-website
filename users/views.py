from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST': #if we get a post request
        form = UserRegisterForm(request.POST)
        #creates a user creation form with our information
        if form.is_valid(): #to validate it
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Your are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#decrators add functionailty to an existing function
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #We would be getting file data within our post
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has beeen Updated')
            return redirect('profile') #important to return a redirect
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    content = {
        "u_form" : u_form,
        'p_form' : p_form,
    }
    return render(request, 'users/profile.html', content)
