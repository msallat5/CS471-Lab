from django.shortcuts import render
from django.http import HttpResponse 

# Lab Week 4 Task 1
#def index(request): 
#    return HttpResponse("Hello, world!")

# Lab Week 4 Task 2
#def index(request): 
#   name = request.GET.get("name")
#   return HttpResponse("Hello, "+name)

# Lab Week 4 Task 3
#def index2(request, val1 = 0):   
#   return HttpResponse("value1 = "+str(val1))

# Lab Week 4 Task 4
#ef index(request): 
#    name = request.GET.get("name") or "world!"
#    return render(request, "bookmodule/index.html")

# Lab Week 4 Task 5
#def index(request): 
#    name = request.GET.get("name") or "world!"
#    return render(request, "bookmodule/index.html" , {"name": name})

# Lab Week 4 Task 7
#def viewbook(request, bookId): 
#    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'} 
#    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
#    targetBook = None 
#    if book1['id'] == bookId: targetBook = book1 
#    if book2['id'] == bookId: targetBook = book2 
#    context = {'book':targetBook}
#    return render(request, 'bookmodule/show.html', context)

# Lab Week 5 (Week 4 Part-1)
def index(request): 
    return render(request, "bookmodule/index.html") 

def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 

def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 

def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html')

# Lab Week 6 (Lab 5)
def links_page(request):
    return render(request, 'bookmodule/links_page.html')

def formatting_page(request):
    return render(request, 'bookmodule/formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')

# Lab 6
def __getBooksList(): 
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3]