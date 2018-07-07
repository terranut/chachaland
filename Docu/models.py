from django.db import models

# Create your models here.

class Enlaces(models.Model):
	enlace=models.CharField(max_length=100)
	pagina=models.ForeignKey('Pagina',on_delete=models.CASCADE)

	def __str__(self):
		return self.enlace


class Categoria(models.Model):
	nombre_cat=models.CharField(max_length=30)

	def __str__(self):
		return self.nombre_cat

class Subcategoria(models.Model):
	nombre_sub=models.CharField(max_length=30)
	categoria=models.ForeignKey('Categoria',on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre_sub

class Pagina(models.Model):
	titulo=models.CharField(max_length=30)
	descripcion=models.TextField()
	codigo=models.TextField(blank=True)
	subpagina=models.ManyToManyField('Pagina',blank=True)
	categoria=models.ForeignKey('Categoria',on_delete=models.CASCADE)
	subcategoria=models.ForeignKey('Subcategoria',on_delete=models.CASCADE)
	

	def __str__(self):
		return self.titulo

