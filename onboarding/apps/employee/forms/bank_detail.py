from django import forms
from onboarding.apps.employee.models.bank_detail import ModelBankingDetail

# ---------------------------------------------------------------------------
# FormBankingDetail
# ---------------------------------------------------------------------------
class FormBankingDetail(forms.ModelForm):
    bank_name = forms.CharField(
        max_length=100, required=True,
        label='Bank Name',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Bank Name'
            })
    )

    ifsc = forms.CharField(
        max_length=100, required=True,
        label='IFSC Code',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'IFSC Code'
            })
    )

    acoount_number = forms.CharField(
        max_length=100, required=True,
        label='Account Number',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Account Number'
            })
    )

    branch_name = forms.CharField(
        max_length=100, required=True,
        label='Branch Name',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Branch Name'
            })
    )

    bank_address = forms.CharField(
        max_length=100, required=True,
        label='Bank Address',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Bank Address'
            })
    )


    state = forms.CharField(
        max_length=100, required=True,
        label='State',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'State'
            })
    )

    bank_post_code = forms.CharField(
        max_length=100, required=True,
        label='Bank Post Code',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Bank Post Code'
            })
    )

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelBankingDetail
        fields = {'bank_name', 'ifsc', 'acoount_number', 'branch_name', 'bank_address', 'state', 'bank_post_code'}
