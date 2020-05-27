from django.db import models
from uuid import uuid4


# -------------------------------------------------------------------------------
# ModelRedirectUrl
# -------------------------------------------------------------------------------
class ModelRedirectUrl(models.Model):
    roles_responsibility = models.BooleanField(default = False)
    personal_info = models.BooleanField(default = False)
    family_info = models.BooleanField(default = False)
    emergency_contact = models.BooleanField(default = False)
    document_gathering = models.BooleanField(default = False)
    drug_declaration = models.BooleanField(default = False)
    bank_detail = models.BooleanField(default = False)
    user = models.IntegerField()

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        db_table = 'redirect_url'
        verbose_name = 'Redirect Url'
        verbose_name_plural = 'Redirect Url'
        managed = True
