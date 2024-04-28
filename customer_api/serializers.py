from rest_framework import serializers
from base.models import Customer, Country, CustomerBusiness

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CustomerBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBusiness
        fields = ['id', 'customer', 'business_category', 'ward', 'name', 'business_registration_date','building_name','building_floor', 'age_of_business']

class CustomerSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    businesses = CustomerBusinessSerializer(many=True, read_only= True)

    class Meta:
        model = Customer
        fields = '__all__'