from django.contrib import admin
from .models import *

@admin.register(justChoice)
class Choice(admin.ModelAdmin):
    fields = ("name","gender")
    list_filter = ("gender",)
    search_fields = ("name",)

admin.site.register([Book,Post,Teacher,Student,Dummy,User])