from django.urls import path
from .views import listings,listing

urlpatterns = [
    path('listings/', listings, name='listings'),
    path('listing/<int:id>/', listing, name='property'),
]