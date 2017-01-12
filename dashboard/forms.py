from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Company
from django.forms import ModelForm


class MyForm(ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

    enrollment_no = forms.CharField(max_length=20)
    id_no = forms.IntegerField()
    cgpa = forms.FloatField()
    # resume = forms.FileField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'enrollment_no', 'id_no', 'cgpa', 'password', 'confirm_password']



