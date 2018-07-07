from django.shortcuts import render
from Wikipy.models import *
from Wikipy.forms import *
from django.shortcuts import redirect
#from django.conf import settings
from django.urls import path
from django.db.models import Q


# Create your views here.
def activeEditon(request,switch):
	admin = Administrador.objects.get(id=1)

	if switch=='on':
		admin.editor =1
	elif switch=='off':
		admin.editor =0

	admin.save()
	
	return redirect('/wiki')



def editon():
	e=Administrador.objects.get(id=1).editor
	return e


################################################################################################


def wiki(request):
	grupos=Grupo.objects.all()
	colores=('#922b21','#76448a','#1f618d','#148f77','#b7950b','#af601a','#283747','#a6acaf')
	

	for grupo in grupos:
		grupo.categorias=Categoria.objects.filter(grupo=grupo.id)

		grupo.total_subcategorias=0

		for categoria in grupo.categorias:

			categoria.num_subcategorias=len(Subcategoria.objects.filter(categoria=categoria.id))
			categoria.subcategorias=Subcategoria.objects.filter(categoria=categoria.id)

			grupo.total_subcategorias+=categoria.num_subcategorias


			count=0
		for categoria in grupo.categorias:
			if	grupo.total_subcategorias >0:

				if count == 8:
					count=0
				categoria.color=colores[count]

				categoria.porcentaje=(len(Subcategoria.objects.filter(categoria=categoria.id))*100) / grupo.total_subcategorias
				count +=1
			
	
	return render(request, 'Wikipy/inicio.html', 
		{'grupos':grupos,
		
		'navigation':'',
		'edit':editon(),
		#'salida':salida,
		#'subcategorias':subcategorias,

		})


################################################################################################


def grupo(request,id_grupo):
	categorias=Categoria.objects.filter(grupo=id_grupo)
	grupos=Grupo.objects.all()
	colores=   ('rgb(255, 64, 0)','rgb(255, 191, 0)','rgb(191, 255, 0)','rgb(0, 153, 0)','rgb(0, 115, 153)','rgb(77, 0, 153)',
                'rgb(153, 0, 153)','rgb(153, 153, 0)','rgb(230, 0, 230)','rgb(102, 153, 153)','rgb(0, 51, 0)','rgb(51, 51, 0)',
                'rgb(102, 51, 0','rgb(204, 51, 0)','rgb(153, 51, 51)','rgb(204, 102, 153)','rgb(153, 51, 255)','rgb(102, 102, 153)',
                'rgb(255, 204, 204)','rgb(0, 51, 102)')



	grupo=Grupo.objects.get(id=id_grupo)
	for categoria in categorias:
		categoria.subcategorias=Subcategoria.objects.filter(categoria=categoria.id)

		count=0
		for subcategoria in categoria.subcategorias:
			subcategoria.num_paginas=len(Pagina.objects.filter(subcategoria=subcategoria.id))
			if count >=20:
				count = 0
				
			subcategoria.color=colores[count]
			count+=1
	

	
	
	return render(request, 'Wikipy/grupo.html', 
		{'grupos':grupos,
		'grupo':grupo,
		'categorias':categorias,
		
		'edit':editon()
		

		})


################################################################################################


def cat(request,id_grupo,id_cat):
	grupos=Grupo.objects.all()
	categorias=Categoria.objects.filter(grupo=id_grupo)
	categoria=Categoria.objects.get(id=id_cat)
	grupo=Grupo.objects.get(id=id_grupo)
	subcategorias=Subcategoria.objects.filter(categoria=id_cat)
	paginas=Pagina.objects.filter(categoria=id_cat)
	
		
	return render(request, 'Wikipy/categorias.html', 
		{'grupos':grupos,
		'grupo':grupo,
		'categorias':categorias,
		'categoria':categoria,
		'subcategorias':subcategorias,
		'paginas':paginas,
		'edit':editon()

		})



################################################################################################
def sub(request,id_grupo,id_cat,id_sub):
	categorias=Categoria.objects.filter(grupo=id_grupo)
	categoria=Categoria.objects.get(id=id_cat)
	grupo=Grupo.objects.get(id=id_grupo)
	grupos=Grupo.objects.all()
	subcategoria=Subcategoria.objects.get(id=id_sub)
	paginas=Pagina.objects.filter(subcategoria=id_sub)

		
	return render(request, 'Wikipy/subcategorias.html', 
		{'grupos':grupos,
		'grupo':grupo,
		'categorias':categorias,
		'categoria':categoria,
		'paginas':paginas,
		'subcategoria':subcategoria,
		'total_paginas':len(paginas),
		'edit':editon()

		})


################################################################################################

def addPag(request,id_sub=0,id_cat=0):

	##Acceder a la pagina de add sin indicar una subcategoria
	if int(id_sub) > 0:
		sub=Subcategoria.objects.get(id=id_sub)
		gr=Categoria.objects.get(id=sub.categoria.id).grupo.id
		grupo=Grupo.objects.get(id=gr)
		categoria=Categoria.objects.get(id=sub.categoria.id)
		subcategoria=Subcategoria.objects.get(id=id_sub)

	else:
		gr=0
		grupo=Categoria.objects.get(id=id_cat).grupo
		categoria=Categoria.objects.get(id=id_cat)
		subcategoria=''
	
	##########################################################

	categorias=Categoria.objects.filter(grupo=grupo.id)
	grupos=Grupo.objects.all()


	##Guardar formulario o formulario con datos
	if request.method == "POST":


		form = PaginaForm(request.POST)

		if form.is_valid():#Comprueba datos correctos y guarda
			pagina=form.save()

			###Si se indica subcategoria redirecciona a pagina recien creada
			if pagina.subcategoria_id:
				categoria=Subcategoria.objects.get(id=pagina.subcategoria_id).categoria
				grupo=Categoria.objects.get(id=categoria.id).grupo
				return redirect('/wiki/grupo/{}/cat/{}/sub/{}'.format(grupo.id,categoria.id,pagina.subcategoria_id))

			##Si no se indica subcategoria es por que se indica categoria y redirecciona a categoria
			else:
				grupo=Categoria.objects.get(id=id_cat).grupo
				return redirect('/wiki/grupo/{}/cat/{}'.format(grupo.id,id_cat))
			####


	##Cargar pagina con formulario en blanco
	else:

		form=PaginaForm(initial={'subcategoria':id_sub,'categoria':id_cat})
		return render(request, 'Wikipy/add_pag.html', 
			{'grupos':grupos,
			'grupo':grupo,
			'form':form,
			'categorias':categorias,
			'categoria':categoria,
			'subcategoria':subcategoria,
			'edit':editon(),
			

			})
	##########



################################################################################################


def addCat(request,id_grupo):
	grupo=Grupo.objects.get(id=id_grupo)
	grupos=Grupo.objects.all()
	categorias=Categoria.objects.filter(grupo=id_grupo)
	'''
	Si recibe los datos del form por post
	'''
	if request.method == "POST":
		form_cat = CategoriaForm(request.POST)
		cat=form_cat.save()
		return redirect('/wiki/grupo/{}/cat/{}'.format(grupo.id,cat.id))
	
	
	#Si se accede por url /wiki/add/cat
	else:
		form_cat = CategoriaForm(initial={'grupo':id_grupo})

	return render(request, 'Wikipy/add_cat.html', 
		{'grupos':grupos,
		'form':form_cat,
		'grupo':grupo,
		'categorias':categorias,
		'edit':editon(),

		})


################################################################################################


def addSub(request,id_cat,id_grupo):
	grupo=Grupo.objects.get(id=id_grupo)
	grupos=Grupo.objects.all()
	categoria=Categoria.objects.get(id=id_cat)
	categorias=Categoria.objects.filter(grupo=id_grupo)

	if request.method == "POST":
		form_sub = SubcategoriaForm(request.POST)
		sub=form_sub.save()
		return redirect('/wiki/grupo/{}/cat/{}'.format(grupo.id,id_cat))
	
	
	#Si se accede por url /wiki/add/cat
	else:
		form_sub = SubcategoriaForm(initial={'categoria':id_cat})

	return render(request, 'Wikipy/add_sub.html', 
		{'grupos':grupos,
		'form':form_sub,
		'grupo':grupo,
		'categorias':categorias,
		'categoria':categoria,
		'edit':editon(),


		
		})


################################################################################################

def addGr(request):
	grupos=Grupo.objects.all()

	if request.method == 'POST':

		form_gr=GrupoForm(request.POST)
		
		if form_gr.is_valid():
			
			form_gr.save()

		return redirect('/wiki/')
	else:
		form_gr=GrupoForm()


	return render(request, 'Wikipy/add_gr.html', 
		{
		'grupos':grupos,
		#'grupo':grupo,
		#'categorias':categorias,
		'form':form_gr,
		'edit':editon(),
		
		

		})



################################################################################################



def rmPag(request,id_pag,id_sub=0,id_grupo=0,id_cat=0):

	Pagina.objects.filter(id=id_pag).delete()
	if id_sub=='X':
		return cat(request,id_grupo,id_cat)

	else:
		return sub(request,id_grupo,id_cat,id_sub)


def rmSub(request,id_sub,id_grupo,id_cat):
	try:
		Subcategoria.objects.filter(id=id_sub).delete()
	except:
		return cat(request,id_grupo,id_cat)
	finally:
		return cat(request,id_grupo,id_cat)



def rmCat(request,id_cat,id_grupo):
	try:
		Categoria.objects.filter(id=id_cat).delete()
	except:
		return redirect('/wiki/grupo/{}/cat/{}'.format(id_grupo,id_cat))

	return grupo(request,id_grupo)


def rmGr(request,id_grupo):
	try:
		Grupo.objects.filter(id=id_grupo).delete()
	except:
		return redirect('/wiki/grupo/{}'.format(id_grupo))

	return wiki(request)




################################################################################################


def editPag(request,id_pag,id_grupo,id_cat,id_sub):
	grupos=Grupo.objects.all()
	grupo=Grupo.objects.get(id=id_grupo)
	categorias=Categoria.objects.filter(grupo_id=id_grupo)
	categoria=Categoria.objects.get(id=id_cat)

	if int(id_sub) > 0:
		subcategoria=Subcategoria.objects.get(id=id_sub)
	else:
		subcategoria=''


	pagina=Pagina.objects.get(id=id_pag)
	
	if request.POST:
		
		form=PaginaForm(request.POST,instance=pagina)
		form.save()
		if int(id_sub)>0:
			return redirect('/wiki/grupo/{}/cat/{}/sub/{}'.format(id_grupo,id_cat,id_sub))
		else:
			return redirect('/wiki/grupo/{}/cat/{}'.format(id_grupo,id_cat))

	else:
		form=PaginaForm(instance=pagina)


	return render(request, 'Wikipy/add_pag.html', 
			{
			'edit':True,
			'grupos':grupos,
			'grupo':grupo,
			'categorias':categorias,
			'form':form,
			'categoria':categoria,
			'subcategoria':subcategoria,
			'edit':editon(),

			})


def editCat(request,id_grupo,id_cat):
	grupos=Grupo.objects.all()
	grupo=Grupo.objects.get(id=id_grupo)
	categorias=Categoria.objects.filter(grupo_id=id_grupo)
	categoria=Categoria.objects.get(id=id_cat)


	if request.POST:
		form=CategoriaForm(request.POST,instance=categoria)
		form.save()
		return redirect('/wiki/grupo/{}/cat/{}'.format(id_grupo,id_cat))

	else:

		form=CategoriaForm(instance=categoria)


	return render(request, 'Wikipy/add_cat.html', 
			{
			'edit':True,
			'grupos':grupos,
			'grupo':grupo,
			'categorias':categorias,
			'form':form,
			'categoria':categoria,
			'edit':editon(),
			#'subcategoria':subcategoria

			})



################################################################################################

def buscar(request):
	grupos=Grupo.objects.all()

	query = request.GET['busqueda']	

	if query:
		qset=(
			Q(titulo__icontains=query) |
			Q(contenido__icontains=query))

		resultados_paginas=Pagina.objects.filter(qset)


	else:
		resultados_paginas=[]



	return render(request, 'Wikipy/search.html', 
				{
				'buscar':query,
				'resultados_paginas':resultados_paginas,
				'grupos':grupos,
				'edit':editon(),
				#'subcategoria':subcategoria

				})



################################################################################################

def handler500(request):
	grupos=Grupo.objects.all()
	return redirect('https://www.youtube.com/chachalands')

def page_not_found(request):
	grupos=Grupo.objects.all()
	return redirect('https://www.youtube.com/chachalands')


################################################################################################