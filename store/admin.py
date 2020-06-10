from django.contrib import admin
from store.models import Book, Comments


# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Book, BooksAdmin)
admin.site.register(Comments)
