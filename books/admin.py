from django.contrib import admin
from .models import BookInfo, BooksContent


# Register your models here.
admin.site.register(BookInfo)
admin.site.register(BooksContent)