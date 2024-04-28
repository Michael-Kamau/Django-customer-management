from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Customer, CustomerBusiness, Ward, Country, County, SubCounty, BusinessCategory
from .serializers import CustomerSerializer, CustomerBusinessSerializer, WardSerializer,CountrySerializer, CountySerializer, SubCountySerializer, BusinessCategorySerializer

@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def customerDetail(request, id):
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
         serializer = CustomerSerializer(customer,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def customerBusiness(request):
    if request.method == 'GET':
         customer_businesses = CustomerBusiness.objects.all()
         serializer = CustomerBusinessSerializer(customer_businesses, many = True)
         return Response(serializer.data)
    if request.method == 'POST':
         serializer = CustomerBusinessSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def customerBusinessDetails(request, id):
    try:
        customer_business = CustomerBusiness.objects.get(pk=id)
    except CustomerBusiness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer = CustomerBusinessSerializer(customer_business)
           return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerBusinessSerializer(customer_business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            customer_business.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def countries(request):
    if request.method == 'GET':
         countries = Country.objects.all()
         serializer = CountrySerializer(countries, many = True)
         return Response(serializer.data)

    if request.method == 'POST':
         serializer = CountrySerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def counties(request):
    if request.method == 'GET':
         countries = County.objects.all()
         serializer = CountySerializer(countries, many = True)
         return Response(serializer.data)

    if request.method == 'POST':
         serializer = CountySerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def subCounties(request):
    if request.method == 'GET':
         countries = SubCounty.objects.all()
         serializer = SubCountySerializer(countries, many = True)
         return Response(serializer.data)

    if request.method == 'POST':
         serializer = SubCountySerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def wards(request):
    if request.method == 'GET':
         wards = Ward.objects.all()
         serializer = WardSerializer(wards, many = True)
         return Response(serializer.data)

    if request.method == 'POST':
         serializer = WardSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def businessCategories(request):
    if request.method == 'GET':
         wards = BusinessCategory.objects.all()
         serializer = BusinessCategorySerializer(wards, many = True)
         return Response(serializer.data)

    if request.method == 'POST':
         serializer = BusinessCategorySerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

