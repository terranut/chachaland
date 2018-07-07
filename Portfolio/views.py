from django.shortcuts import render
import time

# Create your views here.
def inicio(request):
	today=time.strftime("%d/%m/%y")

	
	if request.GET:

		values=request.GET['mensaje']
	else:
		values='vacio'

	return render(request, 'Portfolio/index.html', {'fecha':today,'values':values})

