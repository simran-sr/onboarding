from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.bank_detail import FormBankingDetail
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

#-------------------------------------------------------------------------------
# ViewHome
#-------------------------------------------------------------------------------
class ViewBankingInfo(LoginRequiredMixin, FormView):
    """
    View to display the Bank Deatils form
    """
    form_class = FormBankingDetail
    template_name = 'employee/bank_detail.html'

    def form_valid(self, form):
        print('............................', form)
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
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(bank_detail=True)
    
    def get_success_url(self):         
        return reverse('employee:employee-handbook', kwargs = {'id': self.kwargs['id']})