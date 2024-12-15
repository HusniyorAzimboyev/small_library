from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .services import *
from .forms import *
from .models import Dummy

def main_page(request):
    return redirect("home/")
def login_deco(func):
    return login_required(func,login_url="login_page")

def login_page(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home_page")
    return render(request,"login.html")
@login_deco
def logout_page(request):
    logout(request)
    return redirect("login_page")

@login_deco
def home_page(request):
    context = {
        "book_count":book_count(),
        "student_count":student_count(),
        "teacher_count":teacher_count(),
        "post_count":post_count()
    }
    return render(request,"index.html",context)


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login_page")
    template_name = "signup.html"

class books_list(generic.ListView):
    model = Book
    template_name = "lists/books.html"
    context_object_name="books"
    ordering = ['-id']
class students_list(generic.ListView):
    model = Student
    template_name = "lists/students.html"
    context_object_name="students"
    ordering = ['-id']
class teachers_list(generic.ListView):
    model = Teacher
    template_name = "lists/teachers.html"
    context_object_name="teachers"
    ordering = ['-id']
def posts(request):
    posts_list = post_count(1)
    context = {
        "posts":posts_list
    }
    return render(request,"lists/posts.html",context)
def createbook(request):
    form = BookCreateForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("books_list")
    return render(request,"create.html",{'form':form,'header':"New Book"})
def createStudent(request):
    form = StudentCreateForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("students_list")
    return render(request,"create.html",{'form':form,'header':"New Student"})
def createTeacher(request):
    form = TeacherCreateForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("teachers_list")
    return render(request,"create.html",{'form':form,'header':"New Teacher"})
def createPost(request):
    form = PostCreateForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect("posts_list")
    return render(request,"create.html",{'form':form,'header':"New Post"})

class dummy_list(generic.ListView):
    model = Dummy
    template_name = "lists/dummy.html"
    context_object_name = "data"

def create_dummy(request):
    if request.method == 'POST':
        form = DummyCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)  
    else:
        form = DummyCreateForm()
    return render(request,"create.html",{"form":form})

def work_with_instance(request,pk):
    # instance = get_object_or_404(Student,pk=pk)
    # print(instance)
    # form = StudentCreateForm(request.POST,instance=instance)
    # return render(request, "create.html",{"form":form})

    instance = get_object_or_404(Student, pk=pk)
    print(f"Editing instance: {instance}")

    if request.method == "POST":
        form = StudentCreateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()  # Updates the existing instance
            return redirect('students_list')  # Replace with your desired URL
    else:
        form = StudentCreateForm(instance=instance)  # Pre-fill the form for editing

    return render(request, "create.html", {"form": form})