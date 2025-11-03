#!/usr/bin/python3
import sys

'''
Reducer de mediaGolesPartido

input: equipo;Local/Visitante\tsuma_goles\tn_partidos
output: equipo;Local/Visitante;media_goles
'''

subproblema = None
n_partidos = 0
suma_goles = 0
media_goles = 0

for claveValor in sys.stdin: 
	equipo_rol, goles, partidos = claveValor.split('\t')
	goles = int(goles) # por defecto era string
	partidos = int(partidos)
	if subproblema == None: # primer equipo
		subproblema = equipo_rol
	if subproblema == equipo_rol: # si sigo con ese equipo, sumo
		n_partidos += partidos
		suma_goles += goles
	else: 
		media_goles = suma_goles/n_partidos		
		print("%s;%.3f" % (subproblema, media_goles)) # emito total de equipo
		# y paso al siguiente equipo
		subproblema = equipo_rol
		n_partidos = partidos
		suma_goles = goles
		media_goles = 0
# emito el último equipo fuera del bucle
media_goles = suma_goles/n_partidos
print("%s;%.3f" % (subproblema, media_goles)) # emito total de equipo
