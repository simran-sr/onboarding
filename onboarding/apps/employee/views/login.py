from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
class ViewAutoLoginOnboard(LoginView):
	def __init__(self):
		print("selff...")