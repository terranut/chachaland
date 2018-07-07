


#########################################################

def tryExcept(func):
	
	
	def wrapper(a,b):
		error=""
		try:
			#Funcion o expresion
			func(a,b)


		except:
			error="Valor incorrecto"
		
		
		#si no genera error(try)
		#cualquier codigo adicional a try para evitar generar excepciones
		#por este codigo ajeno al protegido por try
			error="A-OK"

		return func(a,b)

	return wrapper
	




#########################################################	.



@tryExcept
def divide(a,b):
	
	return a/b




