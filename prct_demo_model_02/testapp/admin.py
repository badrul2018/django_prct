from django.contrib import admin
from testapp.models import EmpModel
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=['user','email']

admin.site.register(EmpModel,EmpAdmin)

