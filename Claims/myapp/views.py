import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext

from .forms import ClaimUser, NewUserForm
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect("dashboard")
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm
    return render(request=request, template_name="myapp/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.info(request, f"You are now logged in as {username}.")
                login(request, user)
                # render(request, 'auth_lifecycle/user_profile.html',
                #        context_instance=RequestContext(request))
                # redirect("login")
                # time.sleep(2)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    if request.user.is_authenticated:
        redirect('dashboard')
    form = AuthenticationForm()
    return render(request=request, template_name="myapp/login.html", context={"login_form": form})


@login_required(login_url='login')
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')


from .models import Form


@login_required(login_url='login')
def homepage(request):
    f = Form.objects.filter(id=request.user).exists()
    return render(request, 'myapp/dashboard.html', {'form': Form.objects.get(id=request.user) if f else 'NULL'})


@login_required(login_url='/login')
def delete_request(request):
    f = Form.objects.filter(id=request.user).exists()
    if f:
        Form.objects.get(id=request.user).delete()
        # redirect('dashboard')
    return redirect('dashboard')



@login_required(login_url='login')
def claims(request):
    if request.method == 'POST':
        form = ClaimUser(data=request.POST, files=request.FILES)
        if form.is_valid():
            f = form.save()
            newx = Form.objects.get(vehicle_num=f.vehicle_num)
            newx.id = request.user
            newx.status = 'In Progress'
            newx.save()
            print("SUCCESS")
            redirect('dashboard')

    form = ClaimUser(instance=Form.objects.get(id=request.user)) if Form.objects.filter(id=request.user).exists() else ClaimUser()
    return render(request, 'myapp/form.html', {'form': form})


