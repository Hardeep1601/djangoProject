from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext
# Create your views here.

from .forms import ClaimUser
from .models import Form


@login_required(login_url='/login')
def claims(request):
    if request.method == 'POST':
        form = ClaimUser(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            print("SUCCESS")
        form = Form.objects.get()
    return render(request, 'myapp/form.html', {'form': ClaimUser()})


def EDitClaimForm(request, vechile_num):
    form = ClaimUser(instance=Form.objects.get(vehicle_num=vechile_num))
    return render(request, 'myapp/form.html', {'form': form})
