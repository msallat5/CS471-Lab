from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')