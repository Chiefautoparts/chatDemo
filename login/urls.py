from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^login$', views.login, name='login'),
	url(r'^createUser$', views.create, name='createUser'),
	url(r'^addUser$', views.add, name='addUser')
]