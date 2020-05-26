import uuid
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from onboarding.apps.employee.models.employee import ModelEmployee
from django.contrib.auth import authenticate, login

# Create your views here.
class ViewAutoLoginOnboard(LoginView):
	
	def get(self, request, id):
		print("idddd--", id)
		employee = ModelEmployee.objects.get(uuid=id)
		username = employee.user.username
		password = 'admin@123'
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			ModelEmployee.objects.filter(uuid=id).update(slug="welcome")
			print("session -- ", request.session)
			return render(request, "employee/welcome.html", {"emp_id":employee.uuid})
		else:
			return HttpResponse("wrong credentials..")