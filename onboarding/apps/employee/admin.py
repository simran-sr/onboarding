from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.personal_details import ModelPersonalDetails
from onboarding.apps.employee.models.family_details import ModelFamilyDetails
from onboarding.apps.employee.models.emergency_contact import ModelEmergencyContact
from onboarding.apps.employee.models.documents import ModelDocumentGathering
from onboarding.apps.employee.models.bank_detail import ModelBankingDetail
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', )


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    # prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'is_staff','is_active', 'email' ),
        }),
    )
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ModelEmployee)
admin.site.register(ModelPersonalDetails)
admin.site.register(ModelFamilyDetails)
admin.site.register(ModelEmergencyContact)
admin.site.register(ModelDocumentGathering)
admin.site.register(ModelBankingDetail)
admin.site.register(ModelRedirectUrl)
