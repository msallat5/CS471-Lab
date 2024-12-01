from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Address2(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zipcode}"

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    addresses = models.ManyToManyField(Address2, related_name="students")

    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title