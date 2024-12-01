from django.urls import path 
from . import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    #Lab10
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/update/<int:id>/', views.update_student, name='update_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

    path('students2/', views.student2_list, name='student2_list'),
    path('students2/add/', views.add_student2, name='add_student2'),
    path('students2/update/<int:id>/', views.update_student2, name='update_student2'),
    path('students2/delete/<int:id>/', views.delete_student2, name='delete_student2'),
    path('addresses2/', views.address2_list, name='address2_list'),
    path('addresses2/add/', views.add_address2, name='add_address2'),

    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/add/', views.add_image, name='add_image'),
    path('gallery/delete/<int:id>/', views.delete_image, name='delete_image'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)