from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl
from onboarding.apps.employee.models.personal_details import ModelPersonalDetails
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.personal_details import ModelPersonalDetails
from onboarding.apps.employee.models.bank_detail import ModelBankingDetail


#-------------------------------------------------------------------------------
# ViewRolesResponsibility
#-------------------------------------------------------------------------------
class ViewEmpHandbook(LoginRequiredMixin, TemplateView):
    """
    View to display the home page
    """
    template_name = 'employee/employee_handbook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ModelEmployee.objects.filter(uuid=self.kwargs['id']).update(slug="complete")
        instance = ModelEmployee.objects.get(uuid=self.kwargs['id'])
        context['personal_details'] = ModelPersonalDetails.objects.get(employee=instance)
        context['user_info'] = self.request.user
        context['bank_details'] = ModelBankingDetail.objects.get(employee=instance)
        # ModelRedirectUrl.objects.filter(user=self.request.user.id).update(roles_responsibility=True)
        return context
    
