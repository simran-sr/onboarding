from django.db import models
from onboarding.apps.employee.models.employee import ModelEmployee

# ---------------------------------------------------------------------------
# ModelBankingDetail
# ---------------------------------------------------------------------------
class ModelBankingDetail(models.Model):
    bank_name = models.CharField(
        max_length=255
    )
    ifsc = models.IntegerField()
    acoount_number = models.IntegerField()
    branch_nme = models.CharField(
        max_length=255
    )
    bank_address = models.CharField(
        max_length=255
    )
    state = models.CharField(
        max_length=255
    )
    bank_post_code = models.IntegerField()

    employee = models.OneToOneField(
        'ModelEmployee',
        on_delete=models.CASCADE
    )
    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        db_table = 'bank_detail'
        verbose_name = 'Bank Detail'
        verbose_name_plural = 'Bank Detail'
        managed = True

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    # def __str__(self):
    #     return self.slug













