"""from datetime import datetime
from dateutil.relativedelta import relativedelta

mesesCuota = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre","enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre","enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

nCuotas = 12
añoActual = 2022
mesActual = "noviembre"
montoActual = 5000
nombreActual = "Mesa"
inicio = mesesCuota.index(mesActual) + 1
fin = inicio + nCuotas

meslist = []
añolist = []

for x in range(inicio,fin):
	meslist.append(mesesCuota[x])

for z in range(1,(nCuotas+1)):
	now = datetime.now()
	new_year = now + relativedelta(months=(z))
	format = new_year.strftime("%Y")
	añolist.append(format)

# print(now)
# print(new_year)

print(meslist)
print(añolist)

hola
"""

class Prueba:

	def lista(self):
		self.listado = ["ana", "pedro", "carlos", "pepe"]
		

	def recibidor(self):
		lista = self.listado
		tuplado = tuple(self.listado)
		return tuplado

prueba1 = Prueba()
prueba1.lista()
tupla = prueba1.recibidor()
print(tupla)