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

    path('',
         ViewHome.as_view(),
         name='home'
         ),

    path('onboarding-login/<uuid:id>',
         ViewAutoLoginOnboard.as_view(),
         name='login'
    ),

    path('logout',
         ViewLogout.as_view(),
         name='logout'
         ),

    path('onboarding-roles-and-responsiblity',
    	ViewRolesResponsibility.as_view(),
    	name='onboarding-roles-and-responsiblity'
    ),

    path('onboarding-personal-info/<uuid:id>',
    	ViewPersonalInfo.as_view(),
    	name='onboarding-personal-info'
    ),

    path('onboarding-family-info/<uuid:id>',
    	ViewFamilyInfo.as_view(),
    	name='onboarding-family-info'
    ),

    path('onboarding-document-info/<uuid:id>',
    	ViewDocumentInfo.as_view(),
    	name='onboarding-document-info'
    ),

    path('onboarding-drug-declaration/<uuid:id>',
    	ViewDrugDeclaration.as_view(),
    	name='onboarding-drug-declaration'
    ),

    path('onboarding-banking-info/<uuid:id>',
    	ViewBankingInfo.as_view(),
    	name='onboarding-banking-info'
    )
]