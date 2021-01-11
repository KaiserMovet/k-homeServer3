from django.contrib import admin
from .models import InternetSpeed, InternetStatus
# Register your models here.

admin.site.register(InternetSpeed)
admin.site.register(InternetStatus)
