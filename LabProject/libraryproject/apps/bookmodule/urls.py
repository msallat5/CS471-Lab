from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.index, name="books.index"), 
    path('list_books/', views.list_books, name="books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links_page, name='links_page'),
    path('html5/text/formatting/', views.formatting_page, name='formatting_page'),
    path('html5/listing/', views.listing_page, name='listing_page'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('search/', views.search, name='search'),
    path('simple/query', views.simple_query, name='books.simple_query'),
    path('complex/query', views.lookup_query, name= 'books.lookup_query'),
    path('lab8/task1', views.book_list_task1, name='book_list_task1'),
    path('lab8/task2', views.book_list_task2, name='book_list_task2'),
    path('lab8/task3', views.book_list_task3, name='book_list_task3'),
    path('lab8/task4', views.book_list_task4, name='book_list_task4'),
    path('lab8/task5', views.book_list_task5, name='book_list_task5'),
    path('students/lab8/task7', views.students_per_city, name='students_per_city'),
]
