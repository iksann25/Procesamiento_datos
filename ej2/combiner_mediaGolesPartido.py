#!/usr/bin/python3
import sys

'''
Combiner de mediaGolesPartido

input: equipo;Local/Visitante\tgoles
output: equipo;Local/Visitante\tsuma_goles\tn_partidos
'''

subproblema = None
n_partidos = 0
suma_goles = 0

for claveValor in sys.stdin: 
	equipo_rol, goles = claveValor.split('\t', 1)
	goles = int(goles) # por defecto era string
	if subproblema == None: 
		subproblema = equipo_rol
	if subproblema == equipo_rol: # si sigo con ese equipo y rol, sumo
		n_partidos += 1
		suma_goles += goles
	else: 
		print("%s\t%s\t%s" % (subproblema, suma_goles, n_partidos)) # emito total de equipo
		# y paso al siguiente equipo
		subproblema = equipo_rol
		n_partidos = 1
		suma_goles = goles
# emito el último equipo fuera del bucle
print("%s\t%s\t%s" % (subproblema, suma_goles, n_partidos)) # emito total de equipo
