from django.contrib import admin
from .models import SuperVisors,labour,Attendance
# Register your models here.
admin.site.site_header='Elite Works - Master Panel'


class labourAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'mobile_number',
        'address',
        'aadhar_number',
        'pan_number',
        'UAN_number',
        )
    list_filter = (
        'name',
        'mobile_number',
        'address',
        'UAN_number',
        )

admin.site.register(SuperVisors)
admin.site.register(labour,labourAdmin)
admin.site.register(Attendance)