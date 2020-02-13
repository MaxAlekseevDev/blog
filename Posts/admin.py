from django.contrib import admin
from Posts.models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = []

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass