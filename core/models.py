from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model (already configured in settings.py)
class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# Patient model
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Owner
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    disease = models.TextField()

    def __str__(self):
        return self.name

# Doctor model
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Patient-Doctor Mapping
class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
