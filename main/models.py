from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1)


	class Meta:
		verbose_name_plural = 'catergories'

	def __str__(self):
		return self.tutorial_category

class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(TutorialCategory, null = True, verbose_name='Category', on_delete=models.SET_NULL)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Series'

	def __str__(self):
		return self.tutorial_series


class tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("Date Published", default = datetime.now())
	tutorial_series = models.ForeignKey(TutorialSeries, null = True, verbose_name='Series', on_delete=models.SET_NULL)
	tutorial_slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.tutorial_title