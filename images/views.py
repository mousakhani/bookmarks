from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from images.forms import ImageCreateForm


@login_required
def image_create(request):
	if request.POST:
		# form is sent
		form = ImageCreateForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_item = form.save(commit=False)

			# assign current user to the item
			new_item.user = request.user
			new_item.save()
			messages.success(request, 'Image added successfully')

			# redirect to new created item detail view
			# redirect to new_item.get_absolute_url
			return redirect(new_item)
	else:
		form = ImageCreateForm(data=request.GET)

	return render(request, 'images/image/create.html', {
		'section': 'images',
		'form': form
	})
