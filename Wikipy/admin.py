from django.contrib import admin
from Wikipy.models import  *

# Register your models here.



class PaginaAdmin(admin.ModelAdmin):
	list_display=('titulo','subcategoria')




admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Grupo)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Administrador)

