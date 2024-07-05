from django.contrib import admin
from . models import Departments,Doctors
from.models import Appointment
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Appointment)

# class AppoinmentAdmin(admin.ModelAdmin):
#     list_display = ('p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date')
#     search_fields = ('p_name', 'doc_name')
#     list_filter = ('booking_date',)

# admin.site.register(Appointment, AppointmentAdmin)