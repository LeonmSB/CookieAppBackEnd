from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CookieSerializer
from .models import Cookie

class CookieList(generics.ListCreateAPIView):
    queryset = Cookie.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = CookieSerializer # tell django what serializer to use

class CookieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cookie.objects.all().order_by('id')
    serializer_class = CookieSerializer