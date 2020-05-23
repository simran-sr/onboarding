from django.views.generic.base import TemplateView


#-------------------------------------------------------------------------------
# ViewHome
#-------------------------------------------------------------------------------
class ViewHome(TemplateView):
    """
    View to display the home page
    """
    template_name = 'employee/home.html'