
# from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Property(models.Model):
    DoesNotExist = None
    objects = ''
    PROPERTY_TYPES = (
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Car', 'Car'),
        ('Land', 'Land'),
        ('Furniture', 'Furniture'),
        ('Commercial', 'Commercial'),
    )
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=100)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    description = models.TextField(blank=True)
    number_of_units = models.IntegerField()


    def __str__(self):
        return f"{self.name} - {self.address} - {self.property_type}"
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Unit(models.Model):
    DoesNotExist = None
    objects = None
    property = models.ForeignKey(Property, related_name= 'units', on_delete=models.CASCADE)
    unit_count = models.CharField(max_length=15)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.property.name} - {self.unit_count}"

class Tenant(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone_number}"

class Lease(models.Model):
    objects = None
    DoesNotExist = None
    tenant = models.ForeignKey(Tenant, related_name='leases', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name='leases', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tenant.name} -{self.unit.is_available} - {self.start_date} - {self.end_date}"


