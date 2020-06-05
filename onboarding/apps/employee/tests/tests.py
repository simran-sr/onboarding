from django.test import TestCase,Client
from django.contrib.auth.models import User
from django.urls import reverse
from onboarding.apps.employee.models.employee import ModelEmployee
from onboarding.apps.employee.forms.emergency_contact import FormEmergencyContact
import unittest
from uuid import uuid4

class TestBasic(TestCase):
	"""Basic tests"""

	def create_whatever(self,username):
		self.user = User.objects.create_user(username=username, email='jacob@gamil.com', password='top_secret')
		return ModelEmployee.objects.create(uuid=uuid4(), user=self.user, slug='welcome')

	def test_employee_creation(self):
		w = self.create_whatever('sim')
		self.assertTrue(isinstance(w, ModelEmployee))

	def test_whatever_list_view(self):
		client = Client()
		w = self.create_whatever('sim2')
		url = reverse('employee:note_list')
		resp = client.get(url)
		self.assertEqual(resp.status_code, 200)
		# self.assertIn(w.title, resp.content)

	def test_valid_form(self):
		# w = self.create_whatever('sim3')
		data = {'contact_1': '9041608769', 'contact_1_relation': 'father', 'contact_2':'9988501095','contact_2_relation':'mother','email':'simran@gmail.com',}
		form = FormEmergencyContact(data=data)
		self.assertTrue(form.is_valid())

	def test_invalid_form(self):
		data = {'contact_1': '9041608769', 'contact_1_relation': 'father', 'contact_2':'9988501095','contact_2_relation':'mother','email':'simran',}
		form = FormEmergencyContact(data=data)
		self.assertFalse(form.is_valid())
