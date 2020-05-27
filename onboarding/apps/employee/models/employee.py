from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


# -------------------------------------------------------------------------------
# ModelEmployee
# -------------------------------------------------------------------------------
class ModelEmployee(models.Model):
	uuid = models.UUIDField(
		primary_key=True,
		default=uuid4,
		editable=False,
		help_text="Unique identification for an account."
	)
	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
	slug = models.CharField(
		max_length=255,
		default = 'onboard'
	)

	# ---------------------------------------------------------------------------
	# Meta
	# ---------------------------------------------------------------------------
	class Meta:
		db_table = 'employee'
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'
		managed = True

	# ---------------------------------------------------------------------------
	# __str__
	# ---------------------------------------------------------------------------
	def __str__(self):
		return str(self.uuid)
