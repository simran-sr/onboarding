from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.emergency_contact import FormEmergencyContact
from onboarding.apps.employee.models.emergency_contact import ModelEmergencyContact
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

#-------------------------------------------------------------------------------
# ViewEmergencyContact
#-------------------------------------------------------------------------------
class ViewEmergencyContact(LoginRequiredMixin, FormView):
    """
    View to display the Emergency Contact info form
    """
    model = ModelEmergencyContact
    form_class = FormEmergencyContact
    template_name = 'employee/emergency_contact.html'

    def get_form(self, form_class=None):
        """
        Check if the user already saved emergency contact details. If so, then show
        the form populated with those details, to let user change them.
        """
        if form_class is None:
            form_class = FormEmergencyContact
            id = self.kwargs['id']
            instance = ModelEmployee.objects.get(uuid=id)
            emergency = ModelEmergencyContact.objects.get(employee=instance)
            return form_class(instance=emergency, **self.get_form_kwargs())

    def form_valid(self, form):
        id = self.kwargs['id']
        instance = ModelEmployee.objects.get(uuid=id)
        data = form.save(commit=False)
        data.employee = instance
        data.save()
        self.update_redirect_table()
        ModelEmployee.objects.filter(uuid=id).update(slug="emergency")
        return FormView.form_valid(self, form)

    def update_redirect_table(self):
        """ Logic to update redirect table will be written 
            Success url will also be changed here.
        """
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(ViewEmergencyContact=True)
    
    def get_success_url(self):
        return reverse('employee:document-info', kwargs = {'id': self.kwargs['id']})

