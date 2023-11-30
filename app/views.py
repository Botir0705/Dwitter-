from django.shortcuts import render, redirect
from .models import Profile, Dweet
from .forms import NewUserForm, LogInForm, DweetForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User



def index(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            author = request.user
            body = form.cleaned_data['body']
            dweet = Dweet.objects.create(author=author, body=body)
            dweet.save()
            return redirect('index')
    
    dweets = Dweet.objects.all().order_by('-created_on')[:7]
    return render(request, 'app/index.html', {'dweets': dweets, 'form': form})


def detail_profile(request, id):
    profile = Profile.objects.get(id=id)
    dweets = Dweet.objects.filter(author=profile.username).order_by('-created_on')
    my_profile = Profile.objects.get(pk=(request.user.id-2))

    if request.method == "POST":
        current_user_profile = request.user.profile # botir
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    

    context = {
        'profile': profile,
        'dweets': dweets,
        'my_profile': my_profile
    }
    return render(request, 'app/my_profile.html', context)


def sign_up(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
        else:
                messages.error(request,"Invalid username or password.")
    else:
        messages.error(request, 'Invalid username or password')
    context = {
        'form': form
    }
    return render(request, 'app/sign_up.html', context)
    

def log_in(request):
    form = LogInForm()
    
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
                
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'app/login.html', {'form': form})


def all_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'app/all_profiles.html', {'profiles': profiles})


def log_out(request):
    logout(request)
    return redirect('log_in')