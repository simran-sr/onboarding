from django.urls.conf import path
from onboarding.apps.employee.views.login import ViewAutoLoginOnboard
from onboarding.apps.employee.views.home import ViewHome
from onboarding.apps.employee.views.logout import ViewLogout
from onboarding.apps.employee.views.roles_responsibility import ViewRolesResponsibility
from onboarding.apps.employee.views.personal_info import ViewPersonalInfo
from onboarding.apps.employee.views.family_info import ViewFamilyInfo
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
    path('roles-and-responsiblity',
    	ViewRolesResponsibility.as_view(),
    	name='roles-and-responsiblity'
    ),
    path('personal-info',
    	ViewPersonalInfo.as_view(),
    	name='personal-info'
    ),
    path('family-info',
    	ViewFamilyInfo.as_view(),
    	name='family-info'
    ),
    path('document-info',
    	ViewDocumentInfo.as_view(),
    	name='document-info'
    ),
    path('drug-declaration',
    	ViewDrugDeclaration.as_view(),
    	name='drug-declaration'
    ),
    path('banking-info',
    	ViewBankingInfo.as_view(),
    	name='banking-info'
    ),
    path('logout',
    	ViewLogout.as_view(),
    	name='logout'
    ),


]