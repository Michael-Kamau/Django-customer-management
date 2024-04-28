from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.customers),
    path('<int:id>', views.customerDetail),
    path('businesses/<int:id>', views.customerBusinesses)
]