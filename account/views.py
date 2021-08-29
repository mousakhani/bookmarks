from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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
					return redirect('account:home')
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


def register(request):
	if request.method == 'POST':
		user_form = UserCreationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password2'])
			new_user.save()
			login(request, new_user)
			return render(request, 'account/register.html', {})
	return render(request, 'account/register.html', {'form': UserCreationForm()})
