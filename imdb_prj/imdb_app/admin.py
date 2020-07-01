from django.contrib import admin
from imdb_app.models import Genre,Movie

# Register your models here.

admin.site.register(Genre)
admin.site.register(Movie)