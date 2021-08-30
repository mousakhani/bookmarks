from django.conf import settings
from django.db import models


# Create your models here.


class Image(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images_created')
	title = models.CharField()
	slug = models.SlugField()
	image = models.ImageField(upload_to='images/%y/%m/%d/')
	description = models.TextField(blank=True)
	created = models.DateField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.title
