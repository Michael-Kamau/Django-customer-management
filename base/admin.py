from django.contrib import admin
from .models import Customer, CustomerBusiness, Country, County, SubCounty, Ward, BusinessCategory

admin.site.register(Customer)
admin.site.register(CustomerBusiness)
admin.site.register(Country)
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Ward)
admin.site.register(BusinessCategory)

