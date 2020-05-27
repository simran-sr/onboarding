from django import forms
from onboarding.apps.employee.models.emergency_contact import ModelEmergencyContact


# -------------------------------------------------------------------------------
# FormEmergencyContact
# -------------------------------------------------------------------------------
class FormEmergencyContact(forms.ModelForm):
    contact_1 = forms.CharField(
        max_length=100, required=True,
        label='First Contact',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Contact'
            })
    )
    contact_1_relation = forms.CharField(
        max_length=100, required=True,
        label='Relation',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Relation with person'
            })
    )
    contact_2 = forms.CharField(
        max_length=100, required=True,
        label='Second Contact',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Second Contact'
            })
    )
    contact_2_relation = forms.CharField(
        max_length=100, required=True,
        label='Relation',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Relation with person'
            })
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                'placeholder': 'somebody@example.com',
            })
    )

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelEmergencyContact
        fields = {'contact_1','contact_1_relation','contact_2', 'contact_2_relation', 'email'}
