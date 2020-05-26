from django import forms
from onboarding.apps.employee.models.personal_details import ModelPersonalDetails

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)


# -------------------------------------------------------------------------------
# FormPersonalDetails
# -------------------------------------------------------------------------------
class FormPersonalDetails(forms.ModelForm):
	age = forms.CharField(
        max_length=100, required=True,
        label='Age',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Age'
            })
    )

	gender = forms.ChoiceField(
		choices = GENDER_CHOICES
	)

	address = forms.CharField(
        max_length=100, required=True,
        label='Address',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Address'
            })
    )

	dob = forms.DateField()

	contact = forms.CharField(
        max_length=100, required=True,
        label='Contact',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Contact'
            })
    )
	post_code = forms.CharField(
        max_length=100, required=True,
        label='Post Code',
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'Post Code'
            })
    )


	# ---------------------------------------------------------------------------
	# Meta
	# ---------------------------------------------------------------------------
	class Meta:

		model = ModelPersonalDetails
		fields = {'age', 'gender', 'address','dob', 'contact', 'post_code'}
