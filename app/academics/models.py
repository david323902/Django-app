from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    email=models.EmailField(null= True, blank = True)
    password= models.CharField(null= True, blank = True)
    status= models.BooleanField(null= True, blank = True)
    cre_at=models.DateTimeField(default=datetime.datetime.now())
    updated_at=models.DateTimeField(default=datetime.datetime.now())
    deleted_at= models.DateTimeField(null= True, blank = True)

    def _str_(self):
         return self.email

class Person(models.Model):
     firstname = models.CharField(max_length=20)
     lastname=models.CharField(max_length=20)
     age = models.IntegerField()
     ident_number=models.CharField(max_length=12, blank=True)
     created_at=models.DateTimeField(default=datetime.datetime.now())
     updated_at=models.DateTimeField(default=datetime.datetime.now())
     deleted_at= models.DateTimeField(null= True, blank = True)
     id_user = models.ForeignKey('User',on_delete=models.CASCADE, blank=False,null=False,default=1)

class Student(models.Model):
    code=models.CharField(null= True, blank = True)
    ide_person = models.IntegerField()
    status= models.BooleanField(null= True, blank = True)
    cre_at=models.DateTimeField(default=datetime.datetime.now())
    updated_at=models.DateTimeField(default=datetime.datetime.now())
    deleted_at= models.DateTimeField(null= True, blank = True)

  

class Identification_types(models.Model):
     name = models.CharField(max_length=20)
     abrev=models.CharField(max_length=20)
     descrip=models.CharField(max_length=20)
     created_at=models.DateTimeField(default=datetime.datetime.now())
     updated_at=models.DateTimeField(default=datetime.datetime.now())
     deleted_at= models.DateTimeField(null= True, blank = True)



class Cities(models.Model):
     name = models.CharField(max_length=20)
     abrev=models.CharField(max_length=20)
     descrip=models.CharField(max_length=20)
     ide_dept = models.IntegerField()
     created_at=models.DateTimeField(default=datetime.datetime.now())
     updated_at=models.DateTimeField(default=datetime.datetime.now())
     deleted_at= models.DateTimeField(null= True, blank = True)

class Departments(models.Model):
     name = models.CharField(max_length=20)
     abrev=models.CharField(max_length=20)
     descrip=models.CharField(max_length=20)
     ide_country = models.IntegerField()
     created_at=models.DateTimeField(default=datetime.datetime.now())
     updated_at=models.DateTimeField(default=datetime.datetime.now())
     deleted_at= models.DateTimeField(null= True, blank = True)

class Countries(models.Model):
     name = models.CharField(max_length=20)
     abrev=models.CharField(max_length=20)
     descrip=models.CharField(max_length=20)
     created_at=models.DateTimeField(default=datetime.datetime.now())
     updated_at=models.DateTimeField(default=datetime.datetime.now())
     deleted_at= models.DateTimeField(null= True, blank = True)
