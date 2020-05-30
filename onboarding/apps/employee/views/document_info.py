from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.documents import FormDocumentGathering
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

#-------------------------------------------------------------------------------
# ViewEmergencyContact
#-------------------------------------------------------------------------------
class ViewDocumentInfo(LoginRequiredMixin, FormView):
    """
    View to display the Emergency Contact info form
    """
    form_class = FormDocumentGathering
    template_name = 'employee/document_info.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            
            instance = ModelEmployee.objects.get(uuid=self.kwargs['id'])
            data = form.save(commit=False)
            data.employee = instance
            data.save()
            # form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def update_redirect_table(self):
        """ Logic to update redirect table will be written 
            Success url will also be changed here.
        """
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(document_gathering=True)
    
    def get_success_url(self):         
        return reverse('employee:personal-info', kwargs = {'id': self.kwargs['id']})

