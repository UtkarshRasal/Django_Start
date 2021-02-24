from django.shortcuts import render
from django.http import HttpResponse
from .models import tutorial

def homepage(request):
	return render(request=request, 
				  template_name="main/home.html",
				  context={"tutorials": tutorial.objects.all()})