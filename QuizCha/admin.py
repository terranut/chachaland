from django.contrib import admin
from QuizCha.models import *

# Register your models here.

class PreguntaAdmin(admin.ModelAdmin):
	list_display=('enunciado','categoria')
	list_filter = ('categoria',)
	fields =('categoria','enunciado','correcta')
	#filter_horizontal=('respuestas_falsas',)
	raw_id_fields=('categoria',)

class FalsasAdmin(admin.ModelAdmin):
	pass


'''
admin.site.register(Pregunta,PreguntaAdmin)
admin.site.register(Falsas,FalsasAdmin)
admin.site.register(Categoria)

'''