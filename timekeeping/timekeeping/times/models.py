from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField


class UserProfile(models.Model):
    user = models.OneToOneField(User, max_length=200, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    email_address = models.EmailField()
    state = models.CharField(max_length=2)
    time_zone = TimeZoneField()
    created_date = models.DateTimeField(auto_created=True)


class UserPunch(models.Model):
    punch_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    punch_time = models.DateTimeField(auto_now=True)
