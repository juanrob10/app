from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import LoginForm
from django.contrib.auth.decorators import user_passes_test

def index(request):
    return render(request, 'main/home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/profile')  # Si el usuario ya está autenticado, redirigir al perfil

    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "¡Has iniciado sesión correctamente!")
                return redirect("/")
            else:
                form.add_error(None, "Usuario o contraseña incorrectos.")  # Agregar error al formulario
        else:
            form.add_error(None, "Por favor, complete los campos correctamente.")  # Agregar error al formulario
           

    else:
        form = LoginForm()

    return render(request, "main/login.html", {"form": form})




@login_required
def profile_view(request):
    return render(request, "main/profile.html", {'user': request.user})



def logout_view(request):
    logout(request)
    messages.success(request, "¡Has salido de sesión correctamente!")
    return redirect('/')




