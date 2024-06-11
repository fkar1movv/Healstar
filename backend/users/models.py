from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from core.models import Hospital


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    passport_id = models.CharField(max_length=50, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"Sys Admin: {self.first_name} {self.last_name}"


class Doctor(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100, default='doctor')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    passport_id = models.CharField(max_length=50, null=True)
    specialization = models.CharField(max_length=150, null=True)
    qualification = models.CharField(max_length=150, null=True)
    experience = models.PositiveIntegerField(null=True)
    hospital = models.ForeignKey(Hospital, related_name='hospital', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    doctor_id = models.CharField(max_length=15)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return f'Doctor: {self.name} {self.surname}'

    class Meta:
        db_table = 'doctor'

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'


class Patient(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100, default='patient')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    passport_id = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    patient_id = models.CharField(max_length=15)

    def __str__(self):
        return f'Patient: {self.name} {self.surname}'

    class Meta:
        db_table = 'patient'

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'
