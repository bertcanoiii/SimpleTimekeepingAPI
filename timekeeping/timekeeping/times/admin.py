from django.contrib import admin
from times.models import UserProfile, UserPunch


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserPunch)
