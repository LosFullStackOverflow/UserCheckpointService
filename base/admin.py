from django.contrib import admin

from .models import User, UserCheckpoint

# Register your models here.
admin.site.register([User, UserCheckpoint])

