from urllib import request

from django import forms
from django.core.files.base import ContentFile
from social_core.utils import slugify

from images.models import Image


class ImageCreateForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('title', 'url', 'description')
		widgets = {
			'url': forms.HiddenInput,
		}

	def clean_url(self):
		url = self.cleaned_data['url']
		valid_extensions = ['jpg', 'jpeg']
		# 1 is number of splits
		extension = url.rstrip('.', 1)[1].lower()
		if extension not in valid_extensions:
			raise forms.ValidationError('The given url does not math valid image extensions')
		return url

	def save(self, commit=True):
		image = super(ImageCreateForm, self).save(commit=False)
		image_url = self.cleaned_data['url']
		name = slugify(self.title)
		extension = image_url.rsplit('.', 1)[1].lower()
		image_name = f'{name}.{extension}'

		# download image from the given url
		response = request.urlopen(image_url)
		# first image refers to Image Model and second image refers to image field in Image Model
		image.image.save(image_name, ContentFile(response.read()), save=False)
		if commit:
			image.save()
		return image
