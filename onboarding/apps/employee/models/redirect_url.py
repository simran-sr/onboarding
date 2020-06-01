from django.db import models
from uuid import uuid4


# -------------------------------------------------------------------------------
# ModelRedirectUrl
# -------------------------------------------------------------------------------
class ModelRedirectUrl(models.Model):
    ViewAutoLoginOnboard = models.BooleanField(default = True)
    ViewRolesResponsibility = models.BooleanField(default = False)
    ViewPersonalInfo = models.BooleanField(default = False)
    ViewFamilyInfo = models.BooleanField(default = False)
    ViewEmergencyContact = models.BooleanField(default = False)
    ViewDocumentInfo = models.BooleanField(default = False)
    ViewDrugDeclaration = models.BooleanField(default = False)
    ViewBankingInfo = models.BooleanField(default = False)
    user = models.IntegerField()

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        db_table = 'redirect_url'
        verbose_name = 'Redirect Url'
        verbose_name_plural = 'Redirect Url'
        managed = True
