from django import forms
import datetime
from onboarding.apps.employee.models.personal_details import ModelPersonalDetails

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)
cur_year = datetime.datetime.today().year
year_range = tuple([i for i in range(cur_year - 40, cur_year)])


# -------------------------------------------------------------------------------
# FormPersonalDetails
# -------------------------------------------------------------------------------
class FormPersonalDetails(forms.ModelForm):
	
	gender = forms.ChoiceField(
		choices = GENDER_CHOICES,
        widget = forms.Select(attrs = {
            'class':'form-control'
        })
	)

	address = forms.CharField(
        required=True,
        label='Address',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            })
    )

	dob = forms.DateField(widget=forms.SelectDateWidget(years=year_range,
        attrs={'class':''}))

	contact = forms.CharField(
        max_length=100, required=True,
        label='Contact',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contact'
            })
    )
	post_code = forms.CharField(
        max_length=100, required=True,
        label='Post Code',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Post Code'
            })
    )


	# ---------------------------------------------------------------------------
	# Meta
	# ---------------------------------------------------------------------------
	class Meta:

		model = ModelPersonalDetails
		fields = { 'gender', 'address','dob', 'contact', 'post_code'}
