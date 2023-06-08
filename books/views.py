from django.http import JsonResponse
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Book
from django.core import serializers
import json
from .serializer import BookSerializer


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class BookView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if kwargs.get('book_id'):
            book = Book.objects.get(pk=kwargs.get('book_id'))
            data = serializers.serialize('json', [book])

        else:
            books = Book.objects.all()
            data = serializers.serialize('json', books)

        return JsonResponse({'data': data})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        date_value = "2023-06-08"
        # formatted_date = format_datetime(date_value)
        book = Book.objects.create(title=data['title'], author=data['author'], published_date=date_value)

        return JsonResponse({'data': serializers.serialize('json', [book]), 'message': 'Book added successfully'})



class UpdateBookView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        if kwargs.get('book_id'):
            book = Book.objects.get(pk=kwargs.get('book_id'))
            data = serializers.serialize('json', [book])

        else:
            books = Book.objects.all()
            data = serializers.serialize('json', books)

        return JsonResponse({'data': data})


    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        book = Book.objects.get(pk=kwargs.get('book_id'))
        # book.title = data['title']
        book.author = data['author']
        # book.published_date = data['published_date']
        book.save()

        return JsonResponse({'data': serializers.serialize('json', [book]), 'message': 'document updated successfully'})

    def delete(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs.get('book_id'))
        book.delete()
        return JsonResponse({'message': 'book deleted successfully'})

