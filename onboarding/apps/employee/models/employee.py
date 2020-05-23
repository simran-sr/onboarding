from django.db import models
from uuid import uuid4

class ModelEmployee(models.Model):
	uid = models.UUIDField(
		primary_key=True,
		default=uuid4,
		editable=False,
		help_text="Unique identification for an account."
	)

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length = 254) 
	password = models.CharField(max_length=100)

	class Meta:
		db_table = 'employee'
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'
		managed = True

	def __str__(self):
		return self.email
