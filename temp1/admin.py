from django.contrib import admin
from .models import department ,roles,employee,otp_verifing
# Register your models here.
admin.site.register(department)
admin.site.register(roles)
admin.site.register(employee)
admin.site.register(otp_verifing)