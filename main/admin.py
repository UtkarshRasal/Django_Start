from django.contrib import admin
from .models import tutorial 
from .models import instructor
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


class instructorsModel(admin.ModelAdmin):
	fieldsets = [
			('Title/date', {'fields': ['instructor_name']}),
			('Content', {'fields' : ['instructor_list']})
		]	

admin.site.register(tutorial, tutorialModel)
admin.site.register(instructor, instructorsModel)