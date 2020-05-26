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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     return context
    
