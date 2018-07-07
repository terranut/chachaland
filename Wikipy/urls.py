from django.urls import path
from Wikipy import views as wikipy





urlpatterns = [
    path('', wikipy.wiki),
   	path('grupo/<slug:id_grupo>', wikipy.grupo),
   	path('grupo/<slug:id_grupo>/cat/<slug:id_cat>', wikipy.cat),
   	path('grupo/<slug:id_grupo>/cat/<slug:id_cat>/sub/<slug:id_sub>', wikipy.sub),

   	
   	#ADD
   	path('add/cat/<slug:id_grupo>', wikipy.addCat),
   	path('add/sub/<slug:id_cat>/<slug:id_grupo>', wikipy.addSub),
   	path('add/pag/<slug:id_sub>', wikipy.addPag),
   	path('add/pag/cat/<slug:id_cat>', wikipy.addPag),
   	path('add/gr', wikipy.addGr),
   	####

   	#REMOVE
   	path('rm/pag/<slug:id_pag>/<slug:id_sub>/<slug:id_grupo>/<slug:id_cat>', wikipy.rmPag),
   	path('rm/sub/<slug:id_sub>/<slug:id_grupo>/<slug:id_cat>', wikipy.rmSub),
   	path('rm/cat/<slug:id_cat>/<slug:id_grupo>', wikipy.rmCat),
   	path('rm/gr/<slug:id_grupo>', wikipy.rmGr),
   	########


   	#EDIT
   	path('edit/pag/<slug:id_pag>/<slug:id_grupo>/<slug:id_cat>/<slug:id_sub>', wikipy.editPag),
   	path('edit/cat/<slug:id_grupo>/<slug:id_cat>', wikipy.editCat),



   	#####
   	path('editon/<slug:switch>', wikipy.activeEditon),


   	path('search', wikipy.buscar),

]



