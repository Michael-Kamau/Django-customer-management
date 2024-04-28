from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCounty(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=100)
    sub_county = models.ForeignKey(SubCounty, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name


class BusinessCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    country = models.ForeignKey(Country,on_delete=models.PROTECT, blank = True, null = True)

    def __str__(self):
        return self.name

class CustomerBusiness(models.Model):
    customer = models.ForeignKey(Customer,related_name='businesses', on_delete = models.CASCADE)
    business_category = models.ForeignKey(BusinessCategory, on_delete=models.PROTECT)
    ward = models.ForeignKey(Ward, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    building_name = models.CharField(max_length=20, default='')
    building_floor = models.CharField(max_length=20,default='')
    business_registration_date = models.DateField()

    @property
    def age_of_business(self):
        from datetime import date
        return (date.today() - self.business_registration_date).days

    def __str__(self):
        return self.name