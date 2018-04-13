from django.contrib import admin

# Register your models here.
from accountability.models import Students, Specialties

admin.site.register(Students)
admin.site.register(Specialties)
