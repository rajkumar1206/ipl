from django.contrib import admin

from .models import IPLSeason, Matches

# Register your models here.
admin.site.register(IPLSeason)
admin.site.register(Matches)