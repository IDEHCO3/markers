from django.shortcuts import render
from rest_framework import generics
from bookmarker.models import Bookmark
from serializers import BookmarkSerializer

# Create your views here.
class BookmarksList(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer