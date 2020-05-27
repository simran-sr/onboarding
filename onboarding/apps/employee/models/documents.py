from django.db import models
from onboarding.apps.employee.models.employee import ModelEmployee

# -------------------------------------------------------------------------------
# ModelDocumentGathering
# -------------------------------------------------------------------------------

class ModelDocumentGathering(models.Model):
    file = models.FileField(
        upload_to="employee/documents/"
    )

    employee = models.ForeignKey(
        'ModelEmployee',
        on_delete=models.CASCADE
    )

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        db_table = "documents"
        verbose_name = "Documents"
        verbose_name_plural = "Documents"


    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the feedback entry.
        """
        return self.files.url

