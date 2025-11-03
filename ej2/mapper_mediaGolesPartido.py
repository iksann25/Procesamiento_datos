#!/usr/bin/python3
import sys

'''
Mapper de mediaGolesPartido

input: las lineas del csv
output: equipo;Local/Visitante\tgoles
'''

# por cada linea (partido):
# me quedo con la info. relevante (resultado, equipo local, eq. visitante)
# extraigo de resultado los goles marcados por cada equipo
# emito pares (equipo;rol(Local o Visitante)\tgoles), 2 resultados por partido

for linea in sys.stdin: 
	linea = linea.strip()

# Añadimos un bloque try-except para manejar líneas con formato incorrecto, 
# como la línea de cabecera o cualquier otra que no tenga los datos esperados.
	try:# me quedo con la información relevante
		linea_parse = linea.split(',')
		resultado = linea_parse[3]
		local = linea_parse[5]
		visitante = linea_parse[6]
		
		goles_local, goles_visit = resultado.split('-')
		goles_local = int(goles_local)
		goles_visit = int(goles_visit)
        
        # Normalizo Alavés y Real
		if local == "Deportivo Alavés":
			local = "Alavés"
		elif local == "R. Sociedad": 
			local = "Real Sociedad"
		if visitante == "Deportivo Alavés":
			visitante = "Alavés"
		elif visitante == "R. Sociedad": 
			visitante = "Real Sociedad"

	# emito 2 pares: clave (equipo; local/visitante), valor (goles)
		print(f"{local};Local\t{goles_local}")
		print(f"{visitante};Visitante\t{goles_visit}")
	
	except (IndexError, ValueError):
		continue

