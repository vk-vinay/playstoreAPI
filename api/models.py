from django.db import models

class app_deatils(models.Model):

	app_id = models.CharField(max_length=300)
	app_name = models.CharField(max_length=50)
	description = models.CharField(max_length=1000)
	updated=models.CharField(max_length=30)
	size=models.CharField(max_length=30)
	version=models.CharField(max_length=40)
	android=models.CharField(max_length=40)

	def __str__(self):
		return self.text
