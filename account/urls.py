from django.urls import path

from account.views import user_login

app_name = 'account'
urlpatterns = [
	path('', user_login, name='user_login')
]
