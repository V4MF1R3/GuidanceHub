from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            Profile.objects.create(user=user, role=role)
            login(request, user)
            print("Redirecting to profile_setup...")
            return redirect('profile_setup')
        else:
            errors = form.errors.as_json()  # Convert errors to JSON
    else:
        form = CustomUserCreationForm()
        errors = None
    
    return render(request, 'register.html', {'form': form, 'errors': errors})



def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard
            else:
                # Authentication failed
                form.add_error(None, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def profile_setup(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to your dashboard or profile
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_setup.html', {'form': form})
