from django.contrib import admin
from .models import tutorial
from .models import TutorialSeries
from .models import TutorialCategory 
from tinymce.widgets import TinyMCE
from django.db import models

class tutorialModel(admin.ModelAdmin):
	fieldsets = [
			('Title/date', {'fields': ['tutorial_title', 'tutorial_published']}),
			('URL', {'fields': ['tutorial_slug']}),
			('Series', {'fields': ['tutorial_series']}),
			('Content', {'fields' : ["tutorial_content"]}),
		]

	formfield_overrides = {
			models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(tutorial, tutorialModel)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)