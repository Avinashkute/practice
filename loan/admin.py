from django.contrib import admin
from .models import crop_loan

# Register your models here.
class crop_admin(admin.ModelAdmin):
    list_display = ('NAME','city','Acres')

admin.site.register(crop_loan,crop_admin)
