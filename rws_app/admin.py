# rws_app/admin.py

from django.contrib import admin
from .models import Work, Bill

# This tells the admin site to show the Work model
admin.site.register(Work)

# This tells the admin site to show the Bill model
admin.site.register(Bill)