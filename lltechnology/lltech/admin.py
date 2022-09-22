from django.contrib import admin
from . models import Customer

# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'email']

    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Customer,AdminCustomer)