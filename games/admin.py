from django.contrib import admin
from .models import Genre, Game, Console


# Classes
class GenreAdmin(admin.ModelAdmin):  # creating a table for admin genre
    list_display = ('id', 'name')


class GameAdmin(admin.ModelAdmin):
    exclude = ('date_created',)  # what fields to exclude, comma there so python does not think its a string
    list_display = ('title', 'number_in_stock', 'daily_rate', 'console')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Game,GameAdmin)
admin.site.register(Console)
