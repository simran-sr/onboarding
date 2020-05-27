from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

#-------------------------------------------------------------------------------
# ViewRolesResponsibility
#-------------------------------------------------------------------------------
class ViewRolesResponsibility(LoginRequiredMixin, TemplateView):
    """
    View to display the home page
    """
    template_name = 'employee/roles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(roles_responsibility=True)
        return context
    
