from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Complex, Contact


@admin.register(Complex)
class ComplexModel(MPTTModelAdmin):
    pass


@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    pass
