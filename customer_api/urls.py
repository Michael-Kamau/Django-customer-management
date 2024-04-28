from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getCustomers),
    path('<int:id>', views.customerDetail)
]