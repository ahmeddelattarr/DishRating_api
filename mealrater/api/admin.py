from django.contrib import admin
from .models import Meal,Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal', 'user', 'stars']
    list_filter = ['meal', 'user']

class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'description']
    # Removed title and description from list_filter
    # You can add other fields here if you have more suitable fields to filter by

admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)
