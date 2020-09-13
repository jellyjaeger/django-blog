from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegisteredform
from django.contrib.auth.decorators import login_required
def registration(request):
    if request.method == 'POST':
        user = UserRegisteredform(request.POST)
        if user.is_valid():
            user.save()
            username=user.cleaned_data.get('username')
            messages.success(request,'Registration for {username} is succesfull '.format(username=username))
            return redirect('login')
    else:
         user = UserRegisteredform()
    return render(request,'registration/formold.html',{
        "users":user
        
    })
@login_required
def profile(request):
    return render(request,'registration/profile.html')   

         

# Create your views here.
