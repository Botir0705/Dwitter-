from django.contrib import admin
from .models import Profile, Dweet
from django.contrib.auth.models import User




admin.site.register(Profile)
admin.site.register(Dweet)
