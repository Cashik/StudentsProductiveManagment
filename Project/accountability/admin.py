from django.contrib import admin

# Register your models here.
from accountability.models import Students, Specialties, Courses, Subjects

admin.site.register(Students)
admin.site.register(Specialties)
admin.site.register(Courses)
admin.site.register(Subjects)
