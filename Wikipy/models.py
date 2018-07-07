from django.db import models

# Create your models here.

class Grupo(models.Model):
	nombre=models.CharField(max_length=20)
	img=models.ImageField(upload_to='img_grupos',blank=True)

	def __str__(self):
		return self.nombre

#################################################################################

class Categoria(models.Model):
	nombre=models.CharField(max_length=50)
	grupo=models.ForeignKey('Grupo',on_delete=models.PROTECT)
	
	def __str__(self):
		return self.nombre



#################################################################################


class Subcategoria(models.Model):
	nombre=models.CharField(max_length=50)
	categoria=models.ForeignKey('Categoria',on_delete=models.PROTECT)
	
	def __str__(self):
		return self.nombre


#################################################################################

class Pagina(models.Model):
	titulo=models.CharField(max_length=100)
	contenido=models.TextField()
	categoria=models.ForeignKey('Categoria',on_delete=models.PROTECT,null=True,blank=True)
	subcategoria=models.ForeignKey('Subcategoria',on_delete=models.PROTECT,null=True,blank=True)
	relacionadas=models.ManyToManyField('Pagina',blank=True)
	puntuacion=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)],default=2)
	visto=models.IntegerField(default=0)



	def __str__(self):
		return self.titulo


#################################################################################

class Administrador(models.Model):
	editor=models.IntegerField(default=0)

	def __str__(self):
		return str(self.editor)






