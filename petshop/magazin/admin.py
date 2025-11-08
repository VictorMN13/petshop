from django.contrib import admin
from .models import Locatie, Animal, Serviciu, Categorie, Brand, Furnizor, Pret_Serviciu, Produs, Oferta

admin.site.site_header = "Panou Administrare PetShop"
admin.site.site_title = "Admin PetShop"
admin.site.index_title = "Bun venit la Gestiunea Magazinului"

class ProdusAdmin(admin.ModelAdmin):
    list_display = ('nume', 'categorie', 'brand', 'pret', 'greutate', 'stoc')
    search_fields = ('nume', 'descriere')
    ordering = ['stoc']
    list_filter = ('categorie', 'brand')
    list_per_page = 5
    fieldsets = (
        ('Informații Principale', {
            'fields': ('nume', 'pret', 'stoc')
        }),
        ('Detalii Opționale (click pentru a extinde)', {
            'fields': ('categorie', 'brand', 'descriere', 'imagine', 'greutate', 'furnizori'),
            'classes': ('collapse',),
        }),
    )

class CategorieAdmin(admin.ModelAdmin):
    search_fields = ('denumire', 'descriere')
    
class BrandAdmin(admin.ModelAdmin):
    search_fields = ('nume', 'descriere')
    
class FurnizorAdmin(admin.ModelAdmin):
    search_fields = ('nume_companie', 'email_contact')

class ServiciiAdmin(admin.ModelAdmin):
    search_fields = ('nume', 'descriere')
    
class AnimalAdmin(admin.ModelAdmin):
    search_fields = ('specie', 'rasa')

class OfertaAdmin(admin.ModelAdmin):
    search_fields = ('nume', 'reducere')
    
class PreturiServiciiAdmin(admin.ModelAdmin):
    search_fields = ('pret', 'durata')

admin.site.register(Locatie)
admin.site.register(Produs, ProdusAdmin)
admin.site.register(Serviciu, ServiciiAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Furnizor, FurnizorAdmin)  
admin.site.register(Pret_Serviciu, PreturiServiciiAdmin)
admin.site.register(Oferta, OfertaAdmin)