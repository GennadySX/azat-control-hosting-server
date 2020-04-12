from django.contrib import admin
from .models import *
# Register your models here.


# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['projectType']
#

admin.site.register(DomainModel)
admin.site.register(ProjectTypeModel)
