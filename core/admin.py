# core/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Film)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Favorite)
