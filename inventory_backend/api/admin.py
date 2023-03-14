from django.contrib import admin
from .models import CustomUser, UserActivities

# Register your models here.

admin.site.register((CustomUser, UserActivities, ))