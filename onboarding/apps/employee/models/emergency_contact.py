from django.db import models


# -------------------------------------------------------------------------------
# ModelDocumentGathering
# -------------------------------------------------------------------------------
class ModelEmergencyContact(models.Model):
    employee = models.OneToOneField(
        'ModelEmployee',
        on_delete=models.CASCADE
    )
    contact_1 = models.IntegerField()
    contact_1_relation = models.CharField(
        max_length=255
    )
    contact_2 = models.IntegerField()
    contact_2_relation = models.CharField(
        max_length=255
    )
    email = models.EmailField(
        max_length=250
    )

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        db_table = 'emergency_contact'
        verbose_name = 'Emergency Contact'
        verbose_name_plural = 'Emergency Contact'
        managed = True
