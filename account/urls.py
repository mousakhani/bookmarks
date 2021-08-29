from django.urls import path

from account.views import user_login, dashboard, home, user_logout

app_name = 'account'
urlpatterns = [
	path('', home, name='home'),
	path('login/', user_login, name='user_login'),
	path('logout/', user_logout, name='logout'),
	path('dashboard/', dashboard, name='dashboard')
]
