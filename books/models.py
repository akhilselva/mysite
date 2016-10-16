from django.db import models

class buy(models.Model):
	author= models.CharField(max_length=140,default='')
	book_title= models.CharField(max_length=140,default='')
	publisher= models.CharField(max_length=140,default='')
	body= models.TextField()
	book_image= models.FileField(null=True, blank=True)
	date= models.DateTimeField()
	
	lang = models.CharField(max_length=25,default='')
	book_name = models.CharField(max_length=140,default='')
	
	def __str__(self):
		return self.book_title