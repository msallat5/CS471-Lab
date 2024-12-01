from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Address, Gallery
from .forms import StudentForm, GalleryForm

from .models import Student2, Address2
from .forms import Student2Form, Address2Form


#Lab 10
# List Students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'usermodule/student_list.html', {'students': students})

# Add Student
def add_student(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'usermodule/add_student.html', {'form': form})

# Update Student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'usermodule/update_student.html', {'form': form, 'student': student})

# Delete Student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'usermodule/delete_student.html', {'student': student})


# List Students
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'usermodule/student2_list.html', {'students': students})

# Add Student
def add_student2(request):
    form = Student2Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('student2_list')
    return render(request, 'usermodule/add_student2.html', {'form': form})

# Update Student
def update_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    form = Student2Form(request.POST or None, instance=student)
    if request.method == 'POST':
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            form.save_m2m()
            return redirect('student2_list')
    return render(request, 'usermodule/update_student2.html', {'form': form, 'student': student})

# Delete Student
def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')
    return render(request, 'usermodule/delete_student2.html', {'student': student})

# List Addresses
def address2_list(request):
    addresses = Address2.objects.all()
    return render(request, 'usermodule/address2_list.html', {'addresses': addresses})

# Add Address
def add_address2(request):
    form = Address2Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('address2_list')
    return render(request, 'usermodule/add_address2.html', {'form': form})


# List all images
def gallery_list(request):
    images = Gallery.objects.all()
    return render(request, 'usermodule/gallery_list.html', {'images': images})

# Add an image
def add_image(request):
    form = GalleryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    return render(request, 'usermodule/add_image.html', {'form': form})

# Delete an image
def delete_image(request, id):
    image = get_object_or_404(Gallery, id=id)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery_list')
    return render(request, 'usermodule/delete_image.html', {'image': image})