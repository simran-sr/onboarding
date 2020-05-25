from django.views.generic.base import TemplateView


#-------------------------------------------------------------------------------
# ViewHome
#-------------------------------------------------------------------------------
class ViewBankingInfo(TemplateView):
    """
    View to display the home page
    """
    template_name = 'employee/home.html'
