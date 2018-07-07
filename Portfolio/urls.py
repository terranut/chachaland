from django.urls import path
from Portfolio import views as Portfolio
from Docu import views as Docu



urlpatterns = [
	path('', Portfolio.inicio),
	#path('contacto/', Portfolio.contacto),
   
]