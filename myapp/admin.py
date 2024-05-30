# myapp/admin.py
from django.contrib import admin
from .models import DataStatic, DataTS

admin.site.register(DataStatic)
admin.site.register(DataTS)