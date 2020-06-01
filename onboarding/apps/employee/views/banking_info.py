from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.apps.employee.forms.bank_detail import FormBankingDetail
from onboarding.apps.employee.models.bank_detail import ModelBankingDetail
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.models.redirect_url import ModelRedirectUrl

#-------------------------------------------------------------------------------
# ViewHome
#-------------------------------------------------------------------------------
class ViewBankingInfo(LoginRequiredMixin, FormView):
    """
    View to display the Bank Deatils form
    """
    model = ModelBankingDetail
    form_class = FormBankingDetail
    template_name = 'employee/bank_detail.html'

    def get_form(self, form_class=None):
        """
        Check if the user already saved bank details. If so, then show
        the form populated with those details, to let user change them.
        """
        if form_class is None:
            form_class = FormBankingDetail
            id = self.kwargs['id']
            instance = ModelEmployee.objects.get(uuid=id)
            bank_detail = ModelBankingDetail.objects.get(employee=instance)
            return form_class(instance=bank_detail, **self.get_form_kwargs())

    def form_valid(self, form):
        id = self.kwargs['id']
        instance = ModelEmployee.objects.get(uuid=id)
        data = form.save(commit=False)
        data.employee = instance
        data.save()
        self.update_redirect_table()
        ModelEmployee.objects.filter(uuid=id).update(slug="bank")
        return FormView.form_valid(self, form)

    def update_redirect_table(self):
        """ Logic to update redirect table will be written 
            Success url will also be changed here.
        """
        ModelRedirectUrl.objects.filter(user=self.request.user.id).update(ViewBankingInfo=True)
    
    def get_success_url(self):         
        return reverse('employee:employee-handbook', kwargs = {'id': self.kwargs['id']})