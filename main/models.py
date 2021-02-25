from django.db import models
from datetime import datetime

class tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("Date Published", default = datetime.now())

	def __str__(self):
		return self.tutorial_title

class instructor(models.Model):
	instructor_name =  models.CharField(max_length=200)
	instructor_list = models.TextField()

	def __str__(self):
		return self.instructor_name


	class Meta:
		db_table="instructors"

