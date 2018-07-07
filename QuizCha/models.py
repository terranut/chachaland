from django.db import models

# Create your models here.

class Categoria(models.Model):
	nombre=models.CharField(max_length=30)

	def __str__(self):
		return self.nombre



##############################################


class Falsas(models.Model):
	respuesta=models.CharField(max_length=100)
	pregunta=models.ForeignKey('Pregunta',on_delete=models.CASCADE)

	def __str__(self):
		return self.respuesta




##############################################


class Pregunta(models.Model):

	enunciado=models.CharField(max_length=175)
	correcta=models.CharField(max_length=100)
	categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
	

	def __str__(self):
		return self.enunciado





