from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.customers),
    path('<int:id>', views.customerDetail),
    path('businesses', views.customerBusiness),
    path('businesses/<int:id>', views.customerBusinessDetails),
    path('business-categories', views.businessCategories),
    path('countries', views.countries),
    path('counties', views.counties),
    path('sub-counties', views.subCounties),
    path('wards', views.wards),
]