from django.contrib import admin
from .models import Movie
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Movie)
class MovieAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'status', 'updated_on')
    search_fields = ('title', 'summary')
    list_filter = ('status', 'updated_on')
    summernote_fields = ('summary')
