from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


class add(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'createUser.html'

# Create your views here.
def login(request):
	print '**LOGIN**' * 20
	return render(request, 'login/login.html')

def create(request):
	print '**CREATEUSER**' * 20
	return render(request, 'login/createUser.html')

def add(request):
	print '**ADDUSER**' * 20