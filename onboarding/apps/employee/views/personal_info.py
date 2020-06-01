from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.personal_details import FormPersonalDetails
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

#-------------------------------------------------------------------------------
# ViewPersonalInfo
#-------------------------------------------------------------------------------
class ViewPersonalInfo(LoginRequiredMixin, FormView):
    """
    View to display the Personal info form
    """
    form_class = FormPersonalDetails
    template_name = 'employee/personal_info.html'

    def form_valid(self, form):
        id = self.kwargs['id']
        instance = ModelEmployee.objects.get(uuid=id)
        data = form.save(commit=False)
        data.employee = instance
        data.save()
        self.update_redirect_table()
        ModelEmployee.objects.filter(uuid=id).update(slug="personal")
        return FormView.form_valid(self, form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            print(form.errors)
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def update_redirect_table(self):
        """ Logic to update redirect table will be written 
            Success url will also be changed here.
        """
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(personal_info=True)
    
    def get_success_url(self):         
        return reverse('employee:family-info', kwargs = {'id': self.kwargs['id']})

