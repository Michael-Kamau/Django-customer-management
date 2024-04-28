from rest_framework import serializers
from base.models import Customer, Country, CustomerBusiness

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'



class CustomerBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBusiness
        fields = '__all__'
        depth = 3



class CustomerSerializer(serializers.ModelSerializer):
    businesses = CustomerBusinessSerializer(many=True, read_only= True)
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), write_only=True, source='country')

    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'country_id', 'date_of_birth','businesses','country']
        depth = 1

    def create(self, validated_data):
         customer = Customer.objects.create(**validated_data)
         return customer

