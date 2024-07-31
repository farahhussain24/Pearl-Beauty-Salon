from django.contrib import admin
from .models import AdminPanel, Stylist, Appointment, Contact

# Register your models here.

admin.site.register(AdminPanel)
admin.site.register(Stylist)
admin.site.register(Appointment)
admin.site.register(Contact)