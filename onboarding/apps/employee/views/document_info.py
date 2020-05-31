from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.documents import FormDocumentGathering
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.documents import ModelDocumentGathering
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

    # ---------------------------------------------------------------------------
    # form_valid
    # ---------------------------------------------------------------------------
    def form_valid(self, form, **kwargs):
        for file in self.request.FILES.getlist("files"):
            instance = ModelEmployee.objects.get(uuid=self.kwargs['id'])
            n = ModelDocumentGathering.objects.create(file=file, employee=instance)
            n.save()
        self.update_redirect_table()
        return FormView.form_valid(self, form)

    def update_redirect_table(self):
        """ Logic to update redirect table will be written
            Success url will also be changed here.
        """
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(document_gathering=True)

    def get_success_url(self):
        return reverse('employee:personal-info', kwargs = {'id': self.kwargs['id']})
