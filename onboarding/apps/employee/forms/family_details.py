from django import forms
from onboarding.apps.employee.models.family_details import ModelFamilyDetails


# -------------------------------------------------------------------------------
# FormFamilyDetails
# -------------------------------------------------------------------------------
class FormFamilyDetails(forms.ModelForm):
	father_name = forms.CharField(
        max_length=100, required=True,
        label='Father Name',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Father Name',
            })
    )

	mother_name = forms.CharField(
        max_length=100, required=True,
        label='Mother Name',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Mother Name',
            })
    )
	siblings = forms.CharField(
        max_length=100, required=True,
        label='Siblings',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Siblings',
            })
    )

	# ---------------------------------------------------------------------------
	# Meta
	# ---------------------------------------------------------------------------
	class Meta:
		class Meta:
			model = ModelFamilyDetails
			fields = {'father_name', 'mother_name', 'siblings')
