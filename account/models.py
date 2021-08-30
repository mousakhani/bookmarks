from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	# user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)

	def __str__(self):
		return self.user.username
