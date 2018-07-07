from django.contrib import admin
from Docu.models import *

# Register your models here.

class PaginaAdmin(admin.ModelAdmin):
	list_display=('titulo','categoria','subcategoria')



class SubCategoriaAdmin(admin.ModelAdmin):
	list_display=('nombre_sub','categoria')


'''
admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Subcategoria,SubCategoriaAdmin)
admin.site.register(Categoria)
admin.site.register(Enlaces)
'''