import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def getDocu(seccion='python'):

	contenidos=[]
	
	with open(BASE_DIR+'/Docu/txt/'+seccion+'.txt') as file:
		for line in file:
			contenidos.append(line.split(','))


	return contenidos

def grint(value):
	return value



def pruebas():
	for i in range(2,4):
		grint(i)