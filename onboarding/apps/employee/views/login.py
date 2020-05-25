import uuid
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from onboarding.apps.employee.models.employee import ModelEmployee
from django.contrib.auth import authenticate, login

# Create your views here.
class ViewAutoLoginOnboard(LoginView):
	def __init__(self):
		print("selff...")
		self.greeting = "Good Day"
	
	def get(self, request, id):
		print(self.kwargs['id'])
		id = self.kwargs['id']
		employee = ModelEmployee.objects.get(uuid=id)
		username = employee.user.username
		password = 'admin@123'
		user = authenticate(request, username=username, password=password)
		print("uuuuuuuu", user)
		if user is not None:
			login(request, user)
			return render(request, "employee/welcome.html")
		else:
			return HttpResponse("wrong credentials..")