from django.contrib import admin
from .models import UserProfile, Company
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from dashboard.models import UserProfile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton


admin.site.register(UserProfile)
admin.site.register(Company)
