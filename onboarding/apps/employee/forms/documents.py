from django import forms
from onboarding.apps.employee.models.documents import ModelDocumentGathering

# -------------------------------------------------------------------------------
# FormDocumentGathering
# -------------------------------------------------------------------------------

class FormDocumentGathering(forms.ModelForm):
    files = forms.FileField(
        required=False,
        label='Files',
        widget=forms.FileInput(
            attrs={
                'multiple': True,
                'type': 'file',
                'id': 'fileupload'
            })
    )
    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        model = ModelDocumentGathering
        fields = {'files'}
