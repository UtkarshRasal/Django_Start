from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from main.models import tutorial
from main.models import instructor
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

def homepage(request):
	return render(request=request, 
				  template_name="main/home.html",
				  context={"tutorials": tutorial.objects.all(), "instructors": instructor.objects.all()})

def register(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username') 
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"Now logged in as {username}")
			return redirect('main:homepage')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = NewUserForm
	return render(request, 'main/Register.html', context={'form': form})

def logout_request(request):
	logout(request)
	messages.info(request, 'Logged out successfully!')
	return redirect('main:homepage')

def login_request(request):
	if request.method == 'POST':
		form = NewUserForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Now logged in as {username}")
				return redirect('main:homepage')
			else:
				messages.error(request, "Invalid username/password")
		else:
			messages.error(request, "Invalid username/password")

	form = NewUserForm()
	return render(request, 'main/login.html', {'form': form})
