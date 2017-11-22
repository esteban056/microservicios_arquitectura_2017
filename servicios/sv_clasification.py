# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: sv_clasification.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): lily's_team
# Version: 1.0 Noviembre 2017
# Descripción:
#
#   Este archivo define el rol de un servicio. Su función general es obtener informacion de una base de datos
#	y realizar la clasificacion de texto hacia positiva o negativa, se crea un objeto JSON y lo manda de regreso
#   
#
#
#
#                                        sv_clasification.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer un JSON que  | - Realiza una coneccion|
#           |    Clasificador de    |    contenga información |   y consulta a una.    | 
#           |     comentarios       | 	 de comentarios de    |   a una base de datos  |
#           |      de twitter       |    twitter relevantes   | - Devuelve un JSON con |
#           |                       |    a una pelicula       |   comentarios de       |
#           |                       |    o serie.             |   twitter con analisis |
#			|						|	                      |   de sentimiento.      |
#           +-----------------------+-------------------------+------------------------+
#                          
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8002/api/v3/information?t=superman
from afinn import Afinn
import sqlite3
from flask import Flask, abort, render_template, request
import json
import os

#definimos el lenguaje para la clasificacion
afinn = Afinn(language = 'en')
app = Flask(__name__)

#esta funcion devuelve si un texto es positivo o negativo
def analize(text):
	return 'positive' if afinn.score(text) > 0 else 'negative'

#direccion de la api hay que notar que el v1 causaba problemas asi que se cambio
@app.route("/api/v3/sentiment", methods=['GET'])
def get_sentiment():
	#obtenemos el nombre de la peticion
	query = request.args.get('t')
	#conectamos con la base de datos
	conn = sqlite3.connect('tweets.db')
	#creamos un objeto cursor para ejecutar sentencias
	cursor = conn.cursor()
	
	#obtenemos los tweets relevantes
	result = cursor.execute("SELECT * FROM Tweets WHERE query='"+query+"'")
	#creamos contenedores para dar formato
	data = {}
	comments = []
	#De la consulta hecha se le da formato de diccionario
	for row in result:
		data['id']=row[0]
		data['text']=row[1]
		data['query']= row[2]
		data['polarity'] = analize(row[1])
		data['username']=row[3]
		comments.append(data)
		data = {}

	#cerramos la coneccion con la base de datos
	conn.close()
	#Regresamos un JSON con la informacion
	return json.dumps(comments)

if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8002))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)