from random import randint
from random import shuffle
import operator
from sorteo.models import Carton

def GenerarCarton(participante):
	numeros_carton = {}
	numeros = []
	celdas = []
	carton = {}
	fila0 = {}
	fila1 = {}
	fila2 = {}
	col = 0
	while col < 9:
		fila = 0
		rango1 = 1 + (col * 10)
		rango2 = 3 + (col * 10)
		while fila<3:
			nuevo_numero = randint(rango1,rango2)
			numeros_carton["celda{}{}".format(col,fila)] = nuevo_numero
			rango1 = rango1 + 3
			rango2 = rango2 + 3
			fila = fila + 1
		col = col + 1
	for k in list(numeros_carton):
		celdas.append(k)
		numeros.append(numeros_carton[k])
	for numero in numeros:
		if numeros.count(numero) == 2:
			numeros.pop(numeros.index(numero))
			celdas.pop(numeros.index(numero))

	keys_fila0 = ["00","10","20","30","40","50","60","70","80"]
	keys_fila1 = ["01","11","21","31","41","51","61","71","81"]
	keys_fila2 = ["02","12","22","32","42","52","62","72","82"]

	contador = 1
	while contador < 5:
		eliminar_par = randint(0,8)
		try:
			keys_fila0.pop(eliminar_par)
			contador = contador + 1
		except: pass

	contador = 1
	while contador < 5:
		eliminar_par = randint(0,8)
		try:
			keys_fila1.pop(eliminar_par)
			contador = contador + 1
		except: pass
		

	contador = 1
	while contador < 5:
		eliminar_par = randint(0,8)
		try:
			keys_fila2.pop(eliminar_par)
			contador = contador + 1
		except: pass

	for key in keys_fila0:
		fila0["celda{}".format(key)] = numeros_carton["celda{}".format(key)]

	for key in keys_fila1:
		fila1["celda{}".format(key)] = numeros_carton["celda{}".format(key)]

	for key in keys_fila2:
		fila2["celda{}".format(key)] = numeros_carton["celda{}".format(key)]
	
	carton_bd = {}
	carton_bd.update(fila0)
	carton_bd.update(fila1)
	carton_bd.update(fila2)

	if len(Carton.objects.all()) == 0:
		IDcarton = 10000
	else:
		ultimoID = Carton.objects.latest()
		IDcarton = int(ultimoID.numero_carton) + 1
	nuevo_carton = Carton(numero_carton="{}".format(IDcarton),
	participante = participante,
	fila1=fila0,
	fila2=fila1,
	fila3=fila2)
	nuevo_carton.save()
	carton["fila00"] = fila0
	carton["fila01"] = fila1
	carton["fila02"] = fila2

	return carton