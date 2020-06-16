from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Patient


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='mat',
            email='mat@wp.pl',
            password='testpass123',
            is_patient=True,
            is_doctor=False
        )
        self.assertEqual(user.username, 'mat')
        self.assertEqual(user.email, 'mat@wp.pl')
        self.assertTrue(user.is_patient)
        self.assertFalse(user.is_doctor)


class PatientTests(TestCase):

    def test_create_patient(self):
        self.user = get_user_model().objects.create_user(
            username='mat',
            email='mat@wp.pl',
            password='testpass123')
        patient = Patient.objects.create(
            user=self.user,
            first_name='mateusz',
            surname='kowalski',
            pesel_number='88888888888',
            phone='123339151',
            day_of_birth='1985-01-25',
            gender='Kobieta',
            street='Opolska',
            house_number='10',
            flat_number='10',
            zip_code='30-663',
            city='Kraków'
        )
        self.assertEqual(patient.first_name, 'mateusz')
        self.assertEqual(patient.surname, 'kowalski')
        self.assertEqual(patient.pesel_number, '88888888888')
        self.assertEqual(patient.phone, '123339151')
        self.assertEqual(patient.day_of_birth, '1985-01-25')
        self.assertEqual(patient.gender, 'Kobieta')
        self.assertEqual(patient.street, 'Opolska')
        self.assertEqual(patient.house_number, '10')
        self.assertEqual(patient.flat_number, '10')
        self.assertEqual(patient.zip_code, '30-663')
        self.assertEqual(patient.city, 'Kraków')
        
    def test_string_representation(self):
        patient = Patient(first_name='Mateusz', surname='kowalski')
        self.assertEqual(str(patient), 'Mateusz kowalski')

    def test_compute_age(self):
        day_of_birth = date(1985, 1, 25)
        patient = Patient(day_of_birth=day_of_birth)
        age = patient.compute_age
        self.assertEqual(age, 35)