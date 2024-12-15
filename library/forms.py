from django.forms import ModelForm,FileInput
from .models import *

class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
class TeacherCreateForm(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
class StudentCreateForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
class DummyCreateForm(ModelForm):
    class Meta:
        model = Dummy
        fields = "__all__"
        widgets = {
        "image": FileInput(attrs={'class': 'form-control'})}