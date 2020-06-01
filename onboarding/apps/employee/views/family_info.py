from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.family_details import FormFamilyDetails
from onboarding.apps.employee.models.family_details import ModelFamilyDetails
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl
from onboarding.apps.employee.models.employee import ModelEmployee

#-------------------------------------------------------------------------------
# ViewHome
#-------------------------------------------------------------------------------
class ViewFamilyInfo(LoginRequiredMixin, FormView):
    """
    View to display the Family info form
    """
    model = ModelFamilyDetails
    form_class = FormFamilyDetails
    template_name = 'employee/family_info.html'

    def get_form(self, form_class=None):
        """
        Check if the user already saved emergency contact details. If so, then show
        the form populated with those details, to let user change them.
        """
        if form_class is None:
            form_class = FormFamilyDetails
            id = self.kwargs['id']
            instance = ModelEmployee.objects.get(uuid=id)
            family_details = ModelFamilyDetails.objects.get(employee=instance)
            return form_class(instance=family_details, **self.get_form_kwargs())

    def form_valid(self, form):
        id = self.kwargs['id']
        instance = ModelEmployee.objects.get(uuid=id)
        data = form.save(commit=False)
        data.employee = instance
        data.save()
        self.update_redirect_table()
        ModelEmployee.objects.filter(uuid=id).update(slug="family")
        return FormView.form_valid(self, form)

    def update_redirect_table(self):
        """ Logic to update redirect table will be written 
            Success url will also be changed here.
        """
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(ViewFamilyInfo=True)

    def get_success_url(self):         
        return reverse('employee:emergency-contact', kwargs = {'id': self.kwargs['id']})
