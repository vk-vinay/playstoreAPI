from django.db import models

class app_deatils(models.Model):
	app_id = models.CharField(null=False,)
	app_name = models.CharField()
	description = models.CharField()
	updated=models.CharField()
	size=models.CharField()
	version=models.CharField()
	android=models.CharField()

	def __str__(self):
		return self.text