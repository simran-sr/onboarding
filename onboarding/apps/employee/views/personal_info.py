from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.personal_details import FormPersonalDetails

#-------------------------------------------------------------------------------
# ViewPersonalInfo
#-------------------------------------------------------------------------------
class ViewPersonalInfo(LoginRequiredMixin, FormView):
    """
    View to display the Personal info form
    """
    form_class = FormPersonalDetails
    template_name = 'employee/personal_info.html'
