from django.contrib import admin
from .models import Watchlist, WatchListItem

admin.site.register(Watchlist)
admin.site.register(WatchListItem)