# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: sv_tweets.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): lily's_team
# Version: 1.0 Noviembre 2017
# Descripción:
#
#   Este archivo define el rol de un servicio. Su función general es obtener comentarios de twitter
#	relevantes a una pelicula o serie y guardarlos en una base de datos
#   
#
#
#
#                                        sv_clasification.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Obtener comentarios  | - Se conecta a la api  |
#           |    Recolector de      |    de twitter que       |   de twitter y obtiene | 
#           |     comentarios       | 	 contengan información|   comentarios          |
#           |      de twitter       |    relevantes           | - Realiza una coneccion|
#           |                       |    a una pelicula       |   y escribe datos a una|
#           |                       |    o serie.             |   a una base de datos  |
#           +-----------------------+-------------------------+------------------------+
#                          

import tweepy
import os
from flask import Flask, abort, render_template, request
import urllib, json
import sqlite3

#Como el api de twitter tiene limite de consultas tenemos llaves de respaldo

#Consumer Key (API Key):	vHX6fdHT8HyDCDZZz7Zj2r842
#Consumer Secret (API Secret):	61q5FrV2kCqLWJsDiwFMwo2IKmKhTPs39GiabhipIJW9exDlhn

#Access Token:	139508564-Gxo1cvJij56nAsm8eNgdR64Ubje13a2Nl9DUqigy
#Access Token Secret:	NSCyuWHOO72k3WA1UURdeXz1XRv0a4aUxVHt1QtwZ6UwS

#Guardamos llaves en constantes
CONSUMERKEY = "vHX6fdHT8HyDCDZZz7Zj2r842"#"UrKYBQjgYs8YKoTvTLPrkIZum"
CONSUMERSECRET = "61q5FrV2kCqLWJsDiwFMwo2IKmKhTPs39GiabhipIJW9exDlhn"#"JgOQnKKRxbJRzRBpcYuCYGiMNHqbOWKkEywnpMGyulGSGTJPgR"
ACCESTOKEN = "139508564-Gxo1cvJij56nAsm8eNgdR64Ubje13a2Nl9DUqigy"#"2858235567-4SeI6G7hGKeomWFlS99jIPGQXlsT0dBVNJhCGMN"
ACCESTOKENSECRET = "NSCyuWHOO72k3WA1UURdeXz1XRv0a4aUxVHt1QtwZ6UwS"#"jzG0nOonMaMyWtZ2yUX7vBvHDqHkcrIfcfDYlSTnkSYw3"



app = Flask(__name__)


@app.route("/api/v2/tweets", methods=['GET'])
def get_tweets():
	#usamos las llaves para genetrar el auth
	auth = tweepy.OAuthHandler(CONSUMERKEY, CONSUMERSECRET)
	auth.set_access_token(ACCESTOKEN, ACCESTOKENSECRET)
	#Obtenemos el nombre de la consulta a realizar
	query = request.args.get("t")
	#Definimos el numero maximo de tweets a guardar
	max_tweets = 100
	#Nos identificamos en la api de twitter con las llaves
	api = tweepy.API(auth)
	#Buscamos comentarios sobre la pelicula relevante
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, lang='en').items(max_tweets)]
	
	#Nos conectamos a una base de datos
	conn = sqlite3.connect('tweets.db')
	#Para evitar errores de string en la base de datos modificamos la configuracion
	conn.text_factory = str
	#creamos un objeto cursor para ejecutar sentencias
	cursor = conn.cursor()
	#Creamos la tabla si no existe
	cursor.execute('CREATE TABLE IF NOT EXISTS Tweets (id text PRIMARY KEY, tweet_text text, query text, username text)')

	#De los comentarios buscados los insertamos en la base de datos
	for tweet in searched_tweets:
		aux = { "id": tweet.id,
                    "tweet_text": tweet.text.encode('utf-8'),
                    "query": query,
                    "username" : tweet.user.name
                    }
		try:
			cursor.execute('INSERT INTO Tweets VALUES (:id, :tweet_text, :query, :username)',aux)
		except sqlite3.IntegrityError:
			pass

	#Guardamos los cambios
	conn.commit()
	#Cerramos la coneccion con la base de datos
	conn.close()
	#Retornamos una pagina vacia junto con el codigo 204 que significa 'No Content'
	return ('', 204)


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8001))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)