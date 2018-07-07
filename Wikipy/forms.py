from django import forms
from Wikipy.models import *


####################################################################################

class PaginaForm(forms.ModelForm):
	
	
	class Meta:
		model = Pagina
		fields = ('titulo','contenido','categoria','subcategoria')

		
		widgets={"contenido":forms.Textarea(attrs={'class':'richtexteditor'}),
				"categoria":forms.Select(attrs={'readonly':True}),
				"subcategoria":forms.Select(attrs={'readonly':True}),


		}
				
		

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		for field in self.Meta.fields:
			if field != 'contenido':
				self.fields[field].widget.attrs.update({'class': 'form-control'})


####################################################################################


class CategoriaForm(forms.ModelForm):

	class Meta:
		model = Categoria
		fields = ('nombre','grupo')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.Meta.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})


####################################################################################

class SubcategoriaForm(forms.ModelForm):

	class Meta:
		model = Subcategoria
		fields = ('nombre','categoria')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.Meta.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})



####################################################################################



class GrupoForm(forms.ModelForm):

	class Meta:
		model = Grupo
		fields = ('nombre','img')
		widgets={"nombre":forms.TextInput(attrs={'class':'form-control'}),
				
				}
		



####################################################################################


