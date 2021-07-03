import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from .forms import ClaimUser, NewUserForm
from .models import Form


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect("login")
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm
    return render(request=request, template_name="myapp/register.html", context={"register_form": form})


# def register_request(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)
#
# 				return redirect('login')
#
# 		context = {'form': form}
# 		return render(request, 'accounts/register.html', context)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.info(request, f"You are now logged in as {username}.")
                login(request, user)
                time.sleep(2)
                return redirect("claim")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="myapp/login.html", context={"login_form": form})


def logoutUser(request):
    logout(request)
    return redirect('login')



# def home(request):
# 	context = {}
# 	return render(request, 'myapp/dashboard.html', context)


@login_required(login_url='login')
def claims(request):
    if request.method == 'POST':
        form = ClaimUser(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            print("SUCCESS")
        form = Form.objects.get()
    return render(request, 'myapp/form.html', {'form': ClaimUser()})


# @login_required(login_url='/login')
def EDitClaimForm(request, vechile_num):
    form = ClaimUser(instance=Form.objects.get(vehicle_num=vechile_num))
    return render(request, 'myapp/form.html', {'form': form})
