from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login as login_user, logout as logout_user
from tsm.models import UserRole

# Create your views here.

def index(request):
    return render(request, 'home.html')

def login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = authenticate(request, username=request.POST.get("username"), password=request.POST.get('password'))
            print(data)
            if data is not None:
                user = login_user(request, data)
                # checking role 
                userRole = UserRole.objects.get(user__username=request.POST.get("username"))
                if userRole.role == "user":
                    return redirect("user_dashboard")
                elif userRole.role == "admin":
                    return redirect("admin_dashboard") 
                elif userRole.role == "staff":
                    return redirect("index")

    return render(request, 'login.html',{'form': form})


def logout(request):
    logout_user(request)
    return redirect('index')


def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save()
            # assign user role 
            loginUser = data
            role = UserRole()
            role.user = loginUser
            role.role = "user"
            role.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})