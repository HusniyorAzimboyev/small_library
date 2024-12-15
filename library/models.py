from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class justChoice(models.Model):
    name=models.CharField(max_length=100)
    genders = (
        ("male","Male"),
        ("female","Female")
    )
    gender = models.CharField(max_length=100,choices=genders)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Just created"
        verbose_name_plural = ("Just created")

class Book(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=True,blank=True)
    author = models.CharField(max_length=120)
    description = models.TextField()
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    grade = models.SmallIntegerField()
    def __str__(self):
        return self.name
class Teacher(models.Model):
    subjects = (
        ("pe","PE"),
        ("physics","Physics"),
        ("maths","Maths"),
        ("literature","Literature")
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    subject = models.CharField(max_length=100,choices=subjects)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150,null=True)
    slug = models.SlugField(null=True,blank=True)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    def __str__(self):
        return self.title

class Dummy(models.Model):
    name=models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')

class User(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.name
