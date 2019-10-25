from django.db import models

# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("Date published")


	def __str__(self):
		return self.tutorial_title


class Destination:
	id: int 
	name: str
	img: str
	desc: str 
	price: int 
