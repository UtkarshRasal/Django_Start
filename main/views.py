from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from main.models import tutorial
from .models import TutorialCategory
from .models import TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


def single_slug(request, single_slug):
	categories = [c.category_slug for c in TutorialCategory.objects.all()]
	if single_slug in categories:
		matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)

		series_urls={}
		for m in matching_series:
			part_one = tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest('tutorial_published')
			series_urls[m] = part_one			
		return render(request, 'main/category.html', {'part_one': series_urls})

	tutorials = [t.tutorial_slug for t in tutorial.objects.all()]
	if single_slug in tutorials:
		return HttpResponse(f"{single_slug} is a tutorial")

	return HttpResponse(f"{single_slug} does not exist")

def homepage(request):
	return render(request=request, 
				  template_name="main/categories.html",
				  context={"categories": TutorialCategory.objects.all()})

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
		form = AuthenticationForm(request=request, data=request.POST)
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

	form = AuthenticationForm()
	return render(request, 'main/login.html', {'form': form})
