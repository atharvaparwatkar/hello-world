from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import MyForm
from django.http import HttpResponseRedirect
from .models import UserProfile, Company


def index(request):
    return render(request, 'dashboard/login.html')


def signup(request):
    form = MyForm(request.POST or None)
    # if request.method == 'POST':
    #     return HttpResponse("POST")

    if form.is_valid():
        user = form.save(commit=False)
        id_no = form.cleaned_data['id_no']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(id_no=id_no, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #  info = UserProfile.objects.filter(user=request.user)
                return redirect('dashboard:info')
            else:
                return HttpResponse("user is none")
    # else:
    #     return HttpResponse("form is not valid")

    context = {
        "form": form,
    }
    return render(request, 'dashboard/signup.html', context)


def info(request):
    if request.method == "POST":
        id_no = request.POST['id_no']
        password = request.POST['password']
        user = authenticate(id_no=id_no, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'dashboard/index.html')