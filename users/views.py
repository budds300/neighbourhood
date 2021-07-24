from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ProfileUpdateForm,UserRegistrationForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Your Account has been created!, You are now able to login')
            return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request,'user/register.html',{'form':form})

def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,instance=request.user)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your access has been updated')
            return redirect('profile')
        else:
            u_from = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {'u_form':u_form,'p_form':p_form}
        return render(request,'user/profile.html', context)