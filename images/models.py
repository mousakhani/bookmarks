from django.conf import settings
from django.db import models

# Create your models here.
from social_core.utils import slugify


class Image(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images_created')
	title = models.CharField(max_length=50)
	slug = models.SlugField()
	url = models.URLField()
	image = models.ImageField(upload_to='images/%y/%m/%d/')
	description = models.TextField(blank=True)
	created = models.DateField(auto_now_add=True, db_index=True)
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Image, self).save()

	def get_absolute_url(self):
		return reversed()

	def __str__(self):
		return self.title
