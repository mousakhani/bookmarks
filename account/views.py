from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from account.forms import LoginForm, UserEditForm, ProfileEditForm
from account.models import Profile


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
					return redirect('account:home', )
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
			Profile.objects.create(user=new_user)
			login(request, new_user)
			return render(request, 'account/register.html', {})
	return render(request, 'account/register.html', {'form': UserCreationForm()})


@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			# return render(request, 'account/home.html', {})
			# return redirect('account:home')
			messages.success(request, 'Profile updated successfully')
		else:
			messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)

	return render(request, 'account/edit.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})
