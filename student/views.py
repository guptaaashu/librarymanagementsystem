from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('books')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')

def first(request):
	return render(request, 'first.html', {})

