from django import forms
from Docu.models import *

class PaginaForm(forms.ModelForm):

	class Meta:
		model = Pagina
		fields = ('titulo', 'descripcion','codigo','categoria','subcategoria','subpagina')