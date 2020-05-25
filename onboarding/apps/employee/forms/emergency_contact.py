from django import forms
from onboarding.apps.employee.models.emergency_contact import ModelEmergencyContact


# -------------------------------------------------------------------------------
# FormEmergencyContact
# -------------------------------------------------------------------------------
class FormEmergencyContact(models.Model):
    father_contact = forms.CharField(
        max_length=100, required=True,
        label='Father Contact',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Father Contact'
            })
    )
    frient_contact = forms.CharField(
        max_length=100, required=True,
        label='Friend Contact',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Friend Contact'
            })
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': '',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                'placeholder': 'somebody@example.com',
            })
    )

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelEmergencyContact
        fields = {'father_contact', 'frient_contact', 'email')
