from django.contrib import admin
from .models import Book

# Enregistrement simple
# admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Colonnes visibles dans la liste
    list_display = ("title", "author", "publication_year")

    # Ajout de filtres latéraux
    list_filter = ("author", "publication_year")

    # Ajout d’une barre de recherche
    search_fields = ("title", "author")
admin.site.register(Book, BookAdmin)
