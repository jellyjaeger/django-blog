from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegisteredform
def registration(request):
    if request.method == 'POST':
        user = UserRegisteredform(request.POST)
        if user.is_valid():
            user.save()
            username=user.cleaned_data.get('username')
            email = user.cleaned_data.get('email')
            messages.success(request,'Registration for {username} is succesfull with email {email}'.format(username=username,email=email))
            return redirect('myblog-home')
    else:
         user = UserRegisteredform()
    return render(request,'registration/formold.html',{
        "users":user
        
    })

# Create your views here.
