# -*- coding: utf-8 -*-
from afinn import Afinn
import sqlite3


afinn = Afinn(language = 'en')

query = 'superman'

conn = sqlite3.connect('tweets.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print cursor.fetchall()
result = cursor.execute("SELECT * FROM Tweets WHERE query='"+query+"'")
for row in result:
	print row
"""
#Devuelve contadores de la distribución de polaridades, es decir, cuántos tweets positivos, neutrales y negativos son.
def parse_response(json_response):
    negative_tweets, positive_tweets, neutral_tweets = 0, 0, 0
    for j in json_response["data"]:
        if int(j["polarity"]) == 0:
            neutral_tweets += 1
        elif int(j["polarity"]) > 0:
            positive_tweets += 1
        elif int(j["polarity"]) < 0:
            negative_tweets += 1
    return negative_tweets, positive_tweets, neutral_tweets


@app.route("/api/v1/analysis", methods=['GET'])
def analysis():

    TWEET_TOPIC = request.args.get("t")

    if TWEET_TOPIC is not None:
        afinn = Afinn()
        tweets = []    

        #La función connect nos permite conectarnos a la base de datos.
        conn = sqlite3.connect('tweets.db')
        #La función cursor() creamos un objeto de tipo cursor para poder ejecutar comandos SQL.
        c = conn.cursor()

        #Obtenemos los comentarios guardados en la base de datos de la película buscada.
        for t in c.execute("SELECT * FROM Tweets WHERE query='{0}'".format(TWEET_TOPIC)):
            #Para no realizar doble procesamiento, desde el momento en obtener desde la base de datos se envían
            #a la librería que realizará la clasificación por análisis de sentimientos del texto de los tweets.
            tweet = {"text": str(t[1]),
                     "query": str(t[2]),
                     "polarity": afinn.score(str(t[1]))}

            tweets.append(tweet)

        #Cerramos la conexión con la base de datos.
        conn.close

        result = {"data": tweets}

        negative_tweets, positive_tweets, neutral_tweets = parse_response(result)

        classification_results = {}

        #Se da forma al JSON de respuesta que recibirá la GUI para mostrar el resultado del analisis de sentimientos.
        classification_results['pos'] = positive_tweets
        classification_results['neg'] = negative_tweets
        classification_results['ntl'] = neutral_tweets
        classification_results['total'] = negative_tweets + positive_tweets + neutral_tweets

        return json.dumps(classification_results)

    else:
        # Se devuelve un error 400 para indicar que el servicio no puede funcionar sin parámetro
        abort(400)
"""