from django.views.generic.base import TemplateView


#-------------------------------------------------------------------------------
# ViewHome
#-------------------------------------------------------------------------------
class ViewDrugDeclaration(TemplateView):
    """
    View to display the home page
    """
    template_name = 'employee/drug_declation.html'
