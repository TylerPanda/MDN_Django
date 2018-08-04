from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

# Register your models here.

# admin.site.register(Author);
"""Define Admin Class"""
class AuthorAdmin(admin.ModelAdmin):
    # pass;
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death');
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

"""Register the admin class with the associated model"""
admin.site.register(Author, AuthorAdmin)

# admin.site.register(Book);
#Register the Admin classes for Books Using decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance;
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # pass;
    list_display = ('title', 'author', 'display_genre');
    inlines = [BooksInstanceInline];

# admin.site.register(BookInstance);
#Register the Admin classes for BookInstance Using decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back');
    fieldsets = (
        (None, {
                'fields': ('book', 'imprint', 'id')
        }),
        ('Available', {
                'fields': ('status', 'due_back')
        })
    )
    # pass;

admin.site.register(Genre);
