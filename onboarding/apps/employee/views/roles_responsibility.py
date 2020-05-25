from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


#-------------------------------------------------------------------------------
# ViewHome
#-------------------------------------------------------------------------------
class ViewRolesResponsibility(LoginRequiredMixin, TemplateView):
    """
    View to display the home page
    """
    template_name = 'employee/roles.html'
