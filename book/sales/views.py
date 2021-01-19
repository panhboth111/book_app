from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


from .models import Book
from .serializers import BookSerializer
# Create your views here.


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


