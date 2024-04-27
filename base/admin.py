from django.contrib import admin
from .models import Customer, CustomerBusiness, Country, County, SubCounty, Ward

admin.site.register(Customer)
admin.site.register(CustomerBusiness)
admin.site.register(Country)
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Ward)

