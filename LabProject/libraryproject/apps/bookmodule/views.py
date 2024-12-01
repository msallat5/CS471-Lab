from django.shortcuts import render
from django.http import HttpResponse 
from .models import Book, Student, Address
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm


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


# Lab 7
def simple_query(request): 
    mybooks=Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 

def lookup_query(request): 
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10] 
    if len(mybooks)>=1: 
        return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
    else: 
        return render(request, 'bookmodule/index.html')
    
# Lab 8
def book_list_task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/book_list_task1.html', {'books': books})

def book_list_task2(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/book_list_task2.html', {'books': books})

def book_list_task3(request):
    books = Book.objects.filter(~Q(edition__gt=2) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu'))
    return render(request, 'bookmodule/book_list_task3.html', {'books': books})

def book_list_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/book_list_task4.html', {'books': books})

def book_list_task5(request):
    book_stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/book_list_task5.html', {'book_stats': book_stats})

def students_per_city(request):
    students_count = Address.objects.annotate(student_count=Count('student')).values('city', 'student_count')
    return render(request, 'bookmodule/students_per_city.html', {'students_count': students_count})


#Lab 9 Part 1
def booklist9(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/booklist9.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = float(request.POST.get('price'))
        edition = int(request.POST.get('edition'))

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            edition=edition
        )
        return redirect('/books/lab9_part1/booklist9')

    return render(request, 'bookmodule/add_book.html')

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = float(request.POST.get('price'))
        book.edition = int(request.POST.get('edition'))
        book.save()
        return redirect('/books/lab9_part1/booklist9')

    return render(request, 'bookmodule/edit_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/books/lab9_part1/booklist9')

#Lab 9 Part 2
# List Books
def booklist2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/booklist2.html', {'books': books})

# Add Book
def add_book2(request):
    form = BookForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/booklist2')
    return render(request, 'bookmodule/add_book2.html', {'form': form})

# Edit Book
def edit_book2(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/books/lab9_part2/booklist2')
    return render(request, 'bookmodule/edit_book2.html', {'form': form, 'book': book})

# Delete Book
def delete_book2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect('/books/lab9_part2/booklist2')
    return render(request, 'bookmodule/delete_book2.html', {'book': book})