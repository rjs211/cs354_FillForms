from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import SignupForm
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # TODO log the user in
            login(request,user)
            return redirect('/accounts/dummy/')
    else:
        form = SignupForm()
    return render(request,'accounts/signup.html',{'form': form})

def dummy_view(request):
    return render(request,'accounts/dummy.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/certifs/')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts/login/')

    # # else:
    # #     form = AuthenticationForm()
    # return render(request,'accounts/login.html',{'form': form})
