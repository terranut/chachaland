from django.urls import path
from Docu import views as Docu



urlpatterns = [
   path('', Docu.docu),
   path('test/', Docu.test),
   path('test/<slug:pagina>', Docu.test),
   path('cat/<slug:categoria>', Docu.categoria),
   path('page/<slug:pagina>', Docu.pagina),
   path('sub/<slug:subcategoria>', Docu.subcategoria),
   path('add/', Docu.addPage),
   
]
