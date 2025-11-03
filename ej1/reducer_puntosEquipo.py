#!/usr/bin/python3
import sys

'''
Cominer y Reducer de puntosEquipo

Input: equipo;ptos

Output: equipo;ptos
'''

subproblema = None
suma_ptos = 0

for claveValor in sys.stdin: 
	equipo, ptos = claveValor.split(';', 1) #había usado ; como separador
	ptos = int(ptos) # por defecto era string
	if subproblema == None: # primer equipo
		subproblema = equipo
	if subproblema == equipo: # si sigo con ese equipo, sumo
		suma_ptos += ptos
	else: # si llega un equipo diferente
		print("%s;%s" % (subproblema, suma_ptos)) # emito total de equipo
		# y paso al siguiente equipo
		subproblema = equipo
		suma_ptos = ptos
# emito el último equipo fuera del bucle
print("%s;%s" % (subproblema, suma_ptos)) 


