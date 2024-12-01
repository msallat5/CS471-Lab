from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .decorators import login_required

from .models import Student, Address, Gallery
from .forms import StudentForm, GalleryForm, RegisterForm

from .models import Student2, Address2
from .forms import Student2Form, Address2Form


#Lab 10
# List Students
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'usermodule/student_list.html', {'students': students})

# Add Student
@login_required
def add_student(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'usermodule/add_student.html', {'form': form})

# Update Student
@login_required
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'usermodule/update_student.html', {'form': form, 'student': student})

# Delete Student
@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'usermodule/delete_student.html', {'student': student})


# List Students
@login_required
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'usermodule/student2_list.html', {'students': students})

# Add Student
@login_required
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
@login_required
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
@login_required
def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')
    return render(request, 'usermodule/delete_student2.html', {'student': student})

# List Addresses
@login_required
def address2_list(request):
    addresses = Address2.objects.all()
    return render(request, 'usermodule/address2_list.html', {'addresses': addresses})

# Add Address
@login_required
def add_address2(request):
    form = Address2Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('address2_list')
    return render(request, 'usermodule/add_address2.html', {'form': form})


# List all images
@login_required
def gallery_list(request):
    images = Gallery.objects.all()
    return render(request, 'usermodule/gallery_list.html', {'images': images})

# Add an image
@login_required
def add_image(request):
    form = GalleryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    return render(request, 'usermodule/add_image.html', {'form': form})

# Delete an image
@login_required
def delete_image(request, id):
    image = get_object_or_404(Gallery, id=id)
    if request.method == 'POST':
        image.delete()
        return redirect('gallery_list')
    return render(request, 'usermodule/delete_image.html', {'image': image})


#Lab11
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('login')
        else:
            messages.error(request, 'Error in registration form. Please check and try again.')
    else:
        form = RegisterForm()
    return render(request, 'usermodule/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            messages.success(request, 'Login successfully.')
            return redirect('/users/students/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'usermodule/login.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')