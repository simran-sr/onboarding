import uuid
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from onboarding.apps.employee.models.employee import ModelEmployee

# Create your views here.
class ViewAutoLoginOnboard(LoginView):
	def __init__(self):
		print("selff...")
		greeting = "Good Day"
	
	def get(self, request, id):
		print(self.kwargs['id'])
		id = self.kwargs['id']
		employee = ModelEmployee.objects.get(id=id)
		print("employeee == ", employee)
		return HttpResponse(self.greeting)