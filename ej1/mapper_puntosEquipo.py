#!/usr/bin/python3
import sys

'''
Mapper de puntosEquipo

input: cada linea del csv (partido)
output: se emiten 2 por partido 
 - local;ptos_local
 - visitante;ptos_visitante
'''

# por cada linea (partido):
# 1) se guarda la información relevante (resultado, equipo local, eq.visitante)
# 2) se calculan los puntos obtenidos por cada equipo en ese partido
# 3) se emiten los pares (equipo, ptos) para cada equipo (2 res. por partido)

for linea in sys.stdin: 
	linea = linea.strip()

# Añadimos un bloque try-except para manejar líneas con formato incorrecto 
# como la línea de cabecera o cualquier otra con formato inesperado
	try:# guardar la información relevante
		linea_parse = linea.split(',')
		resultado = linea_parse[3]
		local = linea_parse[5]
		visitante = linea_parse[6]
		goles_local, goles_visit = resultado.split('-')
		goles_local = int(goles_local) # estaba como string
		goles_visit = int(goles_visit) # estaba como string
        # Normalizar datos
		if local == "Deportivo Alavés":
			local = "Alavés"
		elif local == "R. Sociedad": 
			local = "Real Sociedad"
		if visitante == "Deportivo Alavés":
			visitante = "Alavés"
		elif visitante == "R. Sociedad": 
			visitante = "Real Sociedad" 
	except (IndexError, ValueError):
		continue
	# calcular los ptos obtenidos por cada equipo en el partido
	if goles_local > goles_visit: 
		ptos_local = 3
		ptos_visit = 0
	elif goles_local < goles_visit: 
		ptos_local = 0
		ptos_visit = 3
	else: 
		ptos_local = 1
		ptos_visit = 1
# emitir 2 pares: equipo\tptos
	print(f"{local};{ptos_local}")
	print(f"{visitante};{ptos_visit}")

	
	
