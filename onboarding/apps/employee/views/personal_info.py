from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.personal_details import FormPersonalDetails
from onboarding.apps.employee.models.employee import ModelEmployee

#-------------------------------------------------------------------------------
# ViewPersonalInfo
#-------------------------------------------------------------------------------
class ViewPersonalInfo(LoginRequiredMixin, FormView):
    """
    View to display the Personal info form
    """
    form_class = FormPersonalDetails
    template_name = 'employee/personal_info.html'
    success_url = '/'

    def form_valid(self, form):
        instance = ModelEmployee.objects.get(uuid=self.kwargs['id'])
        data = form.save(commit=False)
        data.employee = instance
        data.save()
        self.update_redirect_table()
        return FormView.form_valid(self, form)

    def update_redirect_table(self):
        """ Logic to update redirect table will be written 
            Success url will also be changed here.
        """
        print("@@@@@")
