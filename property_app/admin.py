
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User, Property, Unit, Tenant, Lease


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   pass
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'property_type', 'address', 'description', 'number_of_units')
    search_fields = ('id', 'name', 'property_type', 'address')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id','property', 'unit_count', 'bedrooms', 'bathrooms', 'rent', 'is_available')
    list_filter = ('property', 'unit_count')
    search_fields = ('property', 'unit_count', 'bedrooms', 'bathrooms')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number')
    search_fields = ('name', 'email')
    list_filter = ('email', 'phone_number')

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'unit', 'start_date', 'end_date', 'rent_amount')
    search_fields = ('tenant__name', 'unit__property__name')
    list_filter = ('start_date', 'end_date')
