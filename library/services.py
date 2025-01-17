from .models import *
from django.db import connection

def data_fetchall(cursor):
    data = cursor.fetchall()
    names = cursor.description
    result = [dict(zip(names[0], i)) for i in data]
    return result
def book_count(do=None):
    if do:
        return Book.objects.all().order_by("-id")
    return (Book.objects.all()).count()
def student_count():
    cursor = connection.cursor()
    cursor.execute("select * from library_student;")
    answer = data_fetchall(cursor)
    return len(answer)
def teacher_count():
    return (Teacher.objects.all().order_by("-id")).count()
def post_count(do=None):
    if do:
        return Post.objects.all().order_by("-id")
    return (Post.objects.all()).count()