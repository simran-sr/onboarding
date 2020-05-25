from django.db import models


# -------------------------------------------------------------------------------
# ModelDocumentGathering
# -------------------------------------------------------------------------------
class ModelEmergencyContact(models.Model):
    employee = models.OneToOneField(
        'ModelEmployee',
        on_delete=models.CASCADE
    )
    father_contact = models.IntegerField()
    frient_contact = models.IntegerField()
    gmail = models.EmailField(
        max_length=50
    )

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        db_table = 'emergency_contact'
        verbose_name = 'Emergency Contact'
        verbose_name_plural = 'Emergency Contact'
        managed = True
