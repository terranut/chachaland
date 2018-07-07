class Grint():
	lista=[]





	def print(self,value):
		self.lista.append(value)

	def iterator(self):
		
		return dict(zip(range(1,1+len(self.lista)),self.lista))



	def getValue(self):
		return self.lista