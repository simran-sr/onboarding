from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl
from onboarding.apps.employee.models.employee import ModelEmployee


#-------------------------------------------------------------------------------
# ViewHome
#-------------------------------------------------------------------------------
class ViewDrugDeclaration(LoginRequiredMixin, TemplateView):
    """
    View to display the home page
    """
    template_name = 'employee/drug_declaration.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs['id']
        context = super().get_context_data(**kwargs)
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(ViewDrugDeclaration=True)
        ModelEmployee.objects.filter(uuid=id).update(slug="drug")
        return context

    def get_success_url(self):
        return reverse('employee:bank-details', kwargs = {'id': self.kwargs['id']})
