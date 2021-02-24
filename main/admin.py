from django.contrib import admin
from .models import tutorial 
from tinymce.widgets import TinyMCE
from django.db import models

class tutorialModel(admin.ModelAdmin):
	fieldsets = [
			('Title/date', {'fields': ['tutorial_title', 'tutorial_published']}),
			('Content', {'fields' : ["tutorial_content"]})
		]

	formfield_overrides = {
			models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(tutorial, tutorialModel)