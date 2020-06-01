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

	def __call__(self, request):
		
		response = self.get_response(request)
		return response

	# def process_request(self, request):
	# 	print("process request --- ", request)

	def process_view(self, request, view_func, *view_args, **view_kwargs):
		user = request.user.id
		current_view = view_func.__name__
		print(user)
		redirect_info = ModelRedirectUrl.objects.filter(user=user)
		if redirect_info and current_view in array_seq:
			redirect_info = redirect_info[0]

			url = request.path.split('/')[1]
			uuid = request.path.split('/')[2]
			if url == 'onboard-login':
				if(redirect_info.ViewAutoLoginOnboard):
					print('ViewAutoLoginOnboard',redirect_info.ViewAutoLoginOnboard )
					new_url = 'roles-and-responsiblity'
					if url != new_url:
						urls = 'employee:'+new_url
						return redirect(reverse(urls, kwargs={'id': uuid}))

			if url == 'roles-and-responsiblity':
				if(redirect_info.ViewRolesResponsibility):
					print('ViewRolesResponsibility',redirect_info.ViewRolesResponsibility )
					new_url = 'personal-info'
					if url != new_url:
						urls = 'employee:'+new_url
						return redirect(reverse(urls, kwargs={'id': uuid}))
					
			if url == 'personal-info':
				if(redirect_info.ViewPersonalInfo):
					print('ViewPersonalInfo',redirect_info.ViewPersonalInfo )
					new_url = 'family-info'
					if url != new_url:
						urls = 'employee:'+new_url
						return redirect(reverse(urls, kwargs={'id': uuid}))
				
			if url == 'family-info':
				if(redirect_info.ViewFamilyInfo):
					print('ViewFamilyInfo',redirect_info.ViewFamilyInfo )
					new_url = 'emergency-contact'
					if url != new_url:
						urls = 'employee:'+new_url
						return redirect(reverse(urls, kwargs={'id': uuid}))
				
			if url == 'emergency-contact':
				if(redirect_info.ViewEmergencyContact):
					print('ViewEmergencyContact',redirect_info.ViewEmergencyContact )
					new_url = 'document-info'
					if url != new_url:
						urls = 'employee:'+new_url
						return redirect(reverse(urls, kwargs={'id': uuid}))
				
			if url == 'document-info':
				if(redirect_info.ViewDocumentInfo):
					new_url = 'drug-declaration'
					if url != new_url:
						urls = 'employee:'+new_url
						return redirect(reverse(urls, kwargs={'id': uuid}))
				
			if url == 'drug-declaration':
				if(redirect_info.ViewDrugDeclaration):
					new_url = 'bank-details'
					if url != new_url:
						urls = 'employee:'+new_url
						return redirect(reverse(urls, kwargs={'id': uuid}))
				
			if url == 'bank-details':
				if(redirect_info.ViewBankingInfo):
					new_url = 'employee-handbook'
					if url != new_url:
						urls = 'employee:'+new_url
						return redirect(reverse(urls, kwargs={'id': uuid}))
				
			
			# for page in array_seq: 
			# 	url_key = self.get_key(redirect_obj[page])
			# 	redirect_to = getattr(redirect_info, page)
			# 	previous_redirect = getattr(redirect_info, url_key)
			# 	print("-------------",redirect_to, previous_redirect, (url != redirect_obj[page]))
			# 	if not redirect_to and not previous_redirect and (url != redirect_obj[page]):
			# 		print("!!!!!", page)
			# 		print("#####", url)
			# 		print("$$$", redirect_obj[page])
			# 		print("@@@@", (url != redirect_obj[page]))
			# 		print("****", url_key)
			# 		urllll = 'employee:'+redirect_obj[page]
			# 		# if (url != redirect_obj[page]):
			# 		return redirect(reverse(urllll, kwargs={'id': uuid}))

	def redirect_function(self, url, new_url, uuid): 
		if url != new_url:
			urls = 'employee:'+new_url
			print(urls)
			return redirect(reverse(urls, kwargs={'id': uuid}))
