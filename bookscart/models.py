from django.db import models

# Create your models here.
class customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
       return self.first_name

class admin_addbooks(models.Model):
    book_name=models.CharField(max_length=100)
    photo=models.FileField()
    price=models.IntegerField()
    author=models.CharField(max_length=100)

class buynow(models.Model):
    book_id=models.IntegerField()
    book_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()
    user_id=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    amount=models.IntegerField()

class payment(models.Model):
    user_id=models.CharField(max_length=100)
    book_id=models.IntegerField()
    total=models.IntegerField()
    status=models.CharField(max_length=100)
