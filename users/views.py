from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm

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
    return render(request, 'users/profile.html')
