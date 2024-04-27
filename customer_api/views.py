from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Customer
from .serializers import CustomerSerializer

@api_view(['GET'])
def getCustomers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many = True)
    return Response(serializer.data)