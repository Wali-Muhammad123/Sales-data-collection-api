from django.urls import path
from .views import SaleAPI
urlpatterns=[
    path('',SaleAPI.as_view())
]
