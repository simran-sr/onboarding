from django.urls.conf import path
from onboarding.apps.employee.views.login import ViewAutoLoginOnboard
from onboarding.apps.employee.views.home import ViewHome
from onboarding.apps.employee.views.logout import ViewLogout
from onboarding.apps.employee.views.roles_responsibility import ViewRolesResponsibility
from onboarding.apps.employee.views.personal_info import ViewPersonalInfo
from onboarding.apps.employee.views.family_info import ViewFamilyInfo
from onboarding.apps.employee.views.emergency_contact import ViewEmergencyContact
from onboarding.apps.employee.views.document_info import ViewDocumentInfo
from onboarding.apps.employee.views.drug_declaration import ViewDrugDeclaration
from onboarding.apps.employee.views.banking_info import ViewBankingInfo

urlpatterns = [
    
    path('onboard-login/<uuid:id>', 
         ViewAutoLoginOnboard.as_view(), 
         name='login'
    ),

    path('', 
         ViewHome.as_view(), 
         name='home'
    ),
    path('roles-and-responsiblity/<uuid:id>',
    	ViewRolesResponsibility.as_view(),
    	name='roles-and-responsiblity'
    ),
    path('personal-info/<uuid:id>',
    	ViewPersonalInfo.as_view(),
    	name='personal-info'
    ),
    path('family-info/<uuid:id>',
    	ViewFamilyInfo.as_view(),
    	name='family-info'
    ),
    path('emergency-contact/<uuid:id>',
    	ViewEmergencyContact.as_view(),
    	name='emergency-contact'
    ),
    path('document-info/<uuid:id>',
    	ViewDocumentInfo.as_view(),
    	name='document-info'
    ),
    path('drug-declaration/<uuid:id>',
    	ViewDrugDeclaration.as_view(),
    	name='drug-declaration'
    ),
    path('banking-info/<uuid:id>',
    	ViewBankingInfo.as_view(),
    	name='banking-info'
    ),
    path('logout',
    	ViewLogout.as_view(),
    	name='logout'
    ),


]