from django.shortcuts import render
from django.template import Template,Context
from django.http import HttpResponse
from QuizCha.models import *
from QuizCha.funciones import *


# Create your views here.

def quiz(request):

	lista=[]

	tupla=(4,6,5,3)


	
	salidas=[
	'En construccion',
	
	]
	
	return render(request, 'QuizCha/index.html', {
		'salidas':salidas

		})
	
