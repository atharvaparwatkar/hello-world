from django.contrib.auth.models import Permission, User, AbstractBaseUser
from django.db import models


class UserProfile(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=20)
    id_no = models.IntegerField(unique=True)
    cgpa = models.FloatField(max_length=10)

    def __str__(self):
        return self.name

    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'id_no'
    is_anonymous = False
    is_authenticated = False


class Company(models.Model):
    student = models.ManyToManyField(UserProfile, blank=True)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
