from django.db import models

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

# -------------------------------------------------------------------------------
# ModelPersonalDetails
# -------------------------------------------------------------------------------
class ModelPersonalDetails(models.Model):
	employee = models.OneToOneField(
		'ModelEmployee',
		on_delete=models.CASCADE
	)
	gender = models.IntegerField(
		choices=GENDER_CHOICES
	)
	address = models.CharField(
		max_length=100
	)
	dob = models.DateField()

	contact = models.IntegerField()
	post_code = models.IntegerField()

	# -------------------------------------------------------------------------------
	# calculate_age
	# -------------------------------------------------------------------------------
	def calculate_age(self):
		today = date.today()

		try:
			birthday = self.dob.replace(year=today.year)
		# raised when birth date is February 29 and the current year is not a leap year
		except ValueError:
			birthday = self.dob.replace(year=today.year, day=born.day - 1)

		if birthday > today:
			return today.year - born.year - 1
		else:
			return today.year - born.year

	# ---------------------------------------------------------------------------
	# Meta
	# ---------------------------------------------------------------------------
	class Meta:
		db_table = 'personal_detail'
		verbose_name = 'Personal Details'
		verbose_name_plural = 'Personal Details'
		managed = True
		permissions = (
           ("view_info", "Can view the personal info"),
           ("create_profile", "Can create a profile"),
     	)
