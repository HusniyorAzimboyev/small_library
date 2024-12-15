from django.urls import path
from .views import *

urlpatterns = [
    path('',main_page,name="main"),
    path('login/',login_page,name="login_page"),
    path('logout/',logout_page,name="logout_page"),
    path('signup/',SignupView.as_view(),name="signup_page"),
    path("home/",home_page,name="home_page"),
    path('books_list/',books_list.as_view(),name="books_list"),
    path('students_list/',students_list.as_view(),name="students_list"),
    path('teachers_list/',teachers_list.as_view(),name="teachers_list"),
    path('posts_list/',posts,name="posts_list"),
    path('create_book',createbook,name="create_book"),
    path('create_student',createStudent,name="create_student"),
    path('create_teacher',createTeacher,name="create_teacher"),
    path('create_post', createPost, name="create_post"),

    path("dummy_list/",dummy_list.as_view(),name="dummy_list"),
    path("create_dummy",create_dummy,name="create_dummy"),

    path("instancing/<pk>",work_with_instance,name="instancing"),
    # path("fakeit/",fakeit,name="FakeData")
    # path('more/',more_data,name="add_new_data")
]
