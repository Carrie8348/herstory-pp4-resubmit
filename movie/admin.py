from django.contrib import admin
from .models import Movie, Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'status', 'updated_on')
    search_fields = ('title', 'summary')
    list_filter = ('status', 'updated_on')
    summernote_fields = ('summary')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'body', 'created_on')
    list_filter = ('created_on', 'name')
    search_fields = ('name', 'email', 'body')