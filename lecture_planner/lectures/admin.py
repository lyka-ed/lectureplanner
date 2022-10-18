from django.contrib import admin

# Register your models here.

from .models import Lecture, Lab

admin.site.register(Lecture)
admin.site.register(Lab)


