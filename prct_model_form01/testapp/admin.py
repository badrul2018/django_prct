from django.contrib import admin
from testapp.models import StudModel

# Register your models here.
class StudAdmin(admin.ModelAdmin):
    list_display=['name','roll','email','mark']

admin.site.register(StudModel,StudAdmin)    