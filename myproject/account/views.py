from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def register_view(request):
        if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                        login(request,form.save())
                        return redirect("/")
        else:
                form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})

def login_view(request):
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                login(request,form.get_user())
                return redirect('taskapp:dashboard')
            
        else:
            form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/') 

def profile_view(request):
    return render(request, "account/profile.html")      
  
