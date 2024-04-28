from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Customer, CustomerBusiness
from .serializers import CustomerSerializer, CustomerBusinessSerializer

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
        pass

    elif request.method == 'DELETE':
        pass
@api_view(['GET','POST'])
def createCustomerBusiness(request):
    if request.method == 'GET':
         customer_businesses = CustomerBusiness.objects.all()
         serializer = CustomerBusinessSerializer(customer_businesses, many = True)
         return Response(serializer.data)
    if request.method == 'POST':
         serializer = CustomerBusinessSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def customerBusinesses(request, id):
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           customer_businesses = CustomerBusiness.objects.filter(customer_id=id)
           serializer = CustomerBusinessSerializer(customer_businesses, many = True)
           return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerBusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

