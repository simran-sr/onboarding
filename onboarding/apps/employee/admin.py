from django.contrib import admin
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.personal_details import ModelPersonalDetails
from onboarding.apps.employee.models.family_details import ModelFamilyDetails
from onboarding.apps.employee.models.emergency_contact import ModelEmergencyContact
from onboarding.apps.employee.models.documents import ModelDocumentGathering
from onboarding.apps.employee.models.bank_detail import ModelBankingDetail




admin.site.register(ModelEmployee)
admin.site.register(ModelPersonalDetails)
admin.site.register(ModelFamilyDetails)
admin.site.register(ModelEmergencyContact)
admin.site.register(ModelDocumentGathering)
admin.site.register(ModelBankingDetail)