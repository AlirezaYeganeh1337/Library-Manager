from django.contrib import admin

from .models import Book, Borrow, Category, Return, Shelf

admin.site.register(Shelf)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Return)
