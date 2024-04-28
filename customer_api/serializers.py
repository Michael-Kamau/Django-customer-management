from rest_framework import serializers
from base.models import Customer, Country, CustomerBusiness, Ward, BusinessCategory, County, SubCounty

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'

class SubCountySerializer(serializers.ModelSerializer):
    county_id = serializers.PrimaryKeyRelatedField(queryset=County.objects.all(), source='county')

    class Meta:
        model = SubCounty
        fields = '__all__'
        depth = 1

class WardSerializer(serializers.ModelSerializer):
    sub_county_id = serializers.PrimaryKeyRelatedField(queryset=SubCounty.objects.all(), source='sub_county')
    class Meta:
        model = Ward
        fields = '__all__'
        depth = 2

class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = '__all__'

class CustomerBusinessSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer')
    ward_id = serializers.PrimaryKeyRelatedField(queryset=Ward.objects.all(), write_only=True, source='ward')
    business_category_id = serializers.PrimaryKeyRelatedField(queryset=BusinessCategory.objects.all(), write_only=True, source='business_category')

    class Meta:
        model = CustomerBusiness
        fields = ['id', 'name', 'business_registration_date', 'business_category_id','business_category','customer_id','ward_id','building_floor','building_name','ward' ]
        depth = 3
    def create(self, validated_data):
         customer_business = CustomerBusiness.objects.create(**validated_data)
         return customer_business



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

