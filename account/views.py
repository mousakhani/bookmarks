from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from account.forms import LoginForm


def home(request):
	return render(request, 'account/home.html', {})


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('account:dashboard')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse(' Username or Password is invalid')
	else:
		form = LoginForm()

	return render(request, 'account/login.html', {'form': form})


def user_logout(request):
	logout(request)
	return redirect('account:home')


@login_required()
def dashboard(request):
	return render(request, 'account/dashboard.html', {'dashboard': 'dashboard'})
