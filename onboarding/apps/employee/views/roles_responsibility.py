from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl
from onboarding.apps.employee.models.employee import ModelEmployee

#-------------------------------------------------------------------------------
# ViewRolesResponsibility
#-------------------------------------------------------------------------------
class ViewRolesResponsibility(LoginRequiredMixin, TemplateView):
    """
    View to display the home page
    """
    template_name = 'employee/roles.html'

    def get_context_data(self, **kwargs):
        id = kwargs.get('id')
        context = super().get_context_data(**kwargs)
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(ViewRolesResponsibility=True)
        ModelEmployee.objects.filter(uuid=id).update(slug="role")
        return context
    
