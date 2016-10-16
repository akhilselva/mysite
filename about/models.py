from django.db import models

class about(models.Model):
	title= models.CharField(max_length=140)
	body= models.TextField()
	date= models.DateTimeField()
	photo1 = models.FileField(null=True, blank=True)
	
	
	def __str__(self):
		return self.title

