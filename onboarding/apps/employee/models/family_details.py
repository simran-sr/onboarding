from django.db import models


# -------------------------------------------------------------------------------
# ModelDocumentGathering
# -------------------------------------------------------------------------------
class ModelFamilyDetails(models.Model):
	employee = models.OneToOneField(
		'ModelEmployee',
		on_delete=models.CASCADE
	)
	father_name = models.CharField(
        max_length=255
    )
	mother_name = models.CharField(
        max_length=255
    )
	siblings = models.CharField(
        max_length=255
    )
	# ---------------------------------------------------------------------------
	# Meta
	# ---------------------------------------------------------------------------
	class Meta:
		db_table = 'family_detail'
		verbose_name = 'Family Details'
		verbose_name_plural = 'Family Details'
		managed = True

	# ---------------------------------------------------------------------------
	# __str__
	# ---------------------------------------------------------------------------
	def __str__(self):
		return self.father_name