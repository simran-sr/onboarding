# from django.urls import redirect
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.urls.base import reverse
from django.shortcuts import render, redirect
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

array_seq = ['ViewAutoLoginOnboard','ViewRolesResponsibility','ViewPersonalInfo','ViewFamilyInfo','ViewEmergencyContact','ViewDocumentInfo','ViewDrugDeclaration','ViewBankingInfo']

redirect_obj = {
	"ViewAutoLoginOnboard" : "onboard-login",
	"ViewPersonalInfo" : "personal-info",
	"ViewRolesResponsibility" : "roles-and-responsiblity",
	"ViewFamilyInfo" : "family-info",
	"ViewEmergencyContact" : "emergency-contact",
	"ViewDocumentInfo" : "document-info",
	"ViewDrugDeclaration" : "drug-declaration",
	"ViewBankingInfo" : "bank-details"

}

class MyMiddleware(MiddlewareMixin):
	def __init__(self, get_response):
		
		self.get_response = get_response
		self.myVar = 'SimRan'

	def __call__(self, request):
		
		response = self.get_response(request)
		# self.process_request(request)
		# self.process_response(request, response)
		return response

	# def process_request(self, request):
	# 	print("process request --- ", request)

	def process_view(self, request, view_func, *view_args, **view_kwargs):
		print("++++++++++++")
		user = request.user.id
		current_view = view_func.__name__
		redirect_info = ModelRedirectUrl.objects.filter(user=user)
		redirect_info = redirect_info[0]

		url = request.path.split('/')[1]
		uuid = request.path.split('/')[2]\

		
		for page in array_seq: 
			redirect_to = getattr(redirect_info, page)
			if not redirect_to:
				urllll = 'employee:'+redirect_obj[page]
				if (url != redirect_obj[page]):
					return redirect(reverse(urllll, kwargs={'id': uuid}))
			else:
				print("###")
