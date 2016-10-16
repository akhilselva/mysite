from django.db import models

class ques(models.Model):
	ques = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()
	subject = models.CharField(max_length=140)
	semester = models.CharField(max_length=140)
	may_16 = models.CharField(max_length=140)
	dec_15 = models.CharField(max_length=140)
	may_15 = models.CharField(max_length=140)
	dec_14 = models.CharField(max_length=140)
	pdf_may_16 = models.FileField(null=True, blank=True)
	pdf_dec_15 = models.FileField(null=True, blank=True)
	pdf_may_15 = models.FileField(null=True, blank=True)
	pdf_dec_14 = models.FileField(null=True, blank=True)
	
	
	def __str__(self):
		return self.subject
		