from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Qualification)
admin.site.register(Candidates)