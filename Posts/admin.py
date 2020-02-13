from django.contrib import admin
from Posts.models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'slug','pub_date', 'tags']
    search_fields = ['title', 'description', 'author']
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author', 'category')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name','email', 'is_auth', 'roles']