from django.contrib import admin
from .models import Reviews


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_on', 'posted_by', 'movie')


admin.site.register(Reviews)
