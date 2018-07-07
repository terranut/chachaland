from django.shortcuts import render
from Docu.funciones import *
from Docu.models import *
from Docu.Grint import *
from os import scandir
from Docu.forms import *
from django.shortcuts import redirect


templates={
	'docu':'Docu/inicio.html',
	'categoria':'Docu/categorias.html',
	'subcategoria':'Docu/subcategorias.html',
	'pagina':'Docu/pagina.html',
	'test':'Docu/interprete.html',

}

# Create your views here.

#vista por defecto en docu/ 
def docu(request):
	navigation=list(Categoria.objects.all())
	#Obtiene todas las categorias
	categorias=list(Categoria.objects.all())
	
	dic_categorias={}
	for categoria in categorias:
		#Obtiene cada subcategoria por cada categoria
		dic_categorias[categoria]=Subcategoria.objects.filter(categoria=categoria)

	return render(request, templates['docu'], 
		{'categorias':dic_categorias,'navigation':navigation})


####################################################


def categoria(request,categoria):
	navigation=list(Categoria.objects.all())
	seccion=str.upper(categoria)

	#Obtiene columnas categoria
	c=Categoria.objects.get(nombre_cat=categoria)
	#Obtiene las subcategorias que pertenecen a la anterior categoria
	subcategorias=Subcategoria.objects.filter(categoria=c.id)

	#contenido={'sub1':['page1','page2'],'sub2':['page1','page2']}
	contenido={}
	for sub in subcategorias:
		#Obtiene las paginas para cada subcategoria
		contenido[sub]=Pagina.objects.filter(subcategoria=sub.id)


	return render(request, templates['categoria'], 
		{'seccion':seccion,'navigation':navigation,'contenido':contenido,})


####################################################

def subcategoria(request,subcategoria):
	navigation=list(Categoria.objects.all())

	return render(
		request, templates['subcategoria'], 
		{'categoria':categoria,'subcategoria':subcategoria,'navigation':navigation})


####################################################




def pagina(request,pagina):
	menu=list(Categoria.objects.all())
	navigation=list(Categoria.objects.all())
	
	contenido= Pagina.objects.get(id=pagina)

	subpaginas=list(Pagina.objects.filter(subpagina__id=pagina))

	enlaces=Enlaces.objects.filter(pagina=pagina)

	#contenido={'sub1':['page1','page2'],'sub2':['page1','page2']}
	enlaces_subpaginas={}
	paginas={}
	for subpagina in subpaginas:
		#Contiene key=Object Pagina = lista[lista de enlaces, lista de paginas]
		enlaces_subpaginas[subpagina]=[
		Enlaces.objects.filter(pagina=subpagina),Pagina.objects.filter(subpagina__id=subpagina.id)]
									
	#list(Pagina.objects.filter(subpagina__id=pagina))


	return render(request, templates['pagina'], {
		'pagina':pagina,
		'navigation':navigation,
		'contenido':contenido,
		'subpaginas':subpaginas,
		'enlaces':enlaces,
		'enlaces_subpaginas':enlaces_subpaginas,

		})



####################################################

def test(request,pagina=0):
	ejercicios=[]

	


	navigation=list(Categoria.objects.all())
	if pagina==0:
		with open('/home/chachaland/Chachaland/Docu/txt/python.py') as f:
			code=f.read()
		python=code
	else:
		p=Pagina.objects.get(id=pagina)
		python=p.codigo


	return render(request, templates['test'], 
		{'python':python,'navigation':navigation,'ejercicios':ejercicios})


########################################################################################################

def addPage(request):
	navigation=list(Categoria.objects.all())
	form=PaginaForm()


	if request.method == "POST":
		form = PaginaForm(request.POST)
		if form.is_valid():
			pagina = form.save()
			return redirect('/docu/page/{}'.format(pagina.id))
			
			
	else:
		form = PaginaForm()


	 


	return render(request, 'Docu/addpage.html', {
		'pagina':'pagina',
		'navigation':navigation,
		'form': form,
		'subpaginas':'',
		'enlaces':'',
		'enlaces_subpaginas':'',

		})