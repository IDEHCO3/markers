from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class BookmarksList(generics.ListCreateAPIView):
    pass

