# -*- coding: utf-8 -*-
import tweepy
import os
from flask import Flask, abort, render_template, request
import urllib, json
import sqlite3
#Consumer Key (API Key):	vHX6fdHT8HyDCDZZz7Zj2r842
#Consumer Secret (API Secret):	61q5FrV2kCqLWJsDiwFMwo2IKmKhTPs39GiabhipIJW9exDlhn

#Access Token:	139508564-Gxo1cvJij56nAsm8eNgdR64Ubje13a2Nl9DUqigy
#Access Token Secret:	NSCyuWHOO72k3WA1UURdeXz1XRv0a4aUxVHt1QtwZ6UwS
CONSUMERKEY = "vHX6fdHT8HyDCDZZz7Zj2r842"#"UrKYBQjgYs8YKoTvTLPrkIZum"
CONSUMERSECRET = "61q5FrV2kCqLWJsDiwFMwo2IKmKhTPs39GiabhipIJW9exDlhn"#"JgOQnKKRxbJRzRBpcYuCYGiMNHqbOWKkEywnpMGyulGSGTJPgR"
ACCESTOKEN = "139508564-Gxo1cvJij56nAsm8eNgdR64Ubje13a2Nl9DUqigy"#"2858235567-4SeI6G7hGKeomWFlS99jIPGQXlsT0dBVNJhCGMN"
ACCESTOKENSECRET = "NSCyuWHOO72k3WA1UURdeXz1XRv0a4aUxVHt1QtwZ6UwS"#"jzG0nOonMaMyWtZ2yUX7vBvHDqHkcrIfcfDYlSTnkSYw3"



app = Flask(__name__)


@app.route("/api/v2/tweets", methods=['GET'])
def get_tweets():

	auth = tweepy.OAuthHandler(CONSUMERKEY, CONSUMERSECRET)
	auth.set_access_token(ACCESTOKEN, ACCESTOKENSECRET)
	query = request.args.get("t")
	max_tweets = 100

	api = tweepy.API(auth)
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=query, lang='en').items(max_tweets)]
	

	conn = sqlite3.connect('tweets.db')
	conn.text_factory = str
	cursor = conn.cursor()

	cursor.execute('CREATE TABLE IF NOT EXISTS Tweets (id text PRIMARY KEY, tweet_text text, query text)')


	for tweet in searched_tweets:
		aux = { "id": tweet.id,
                    "tweet_text": tweet.text.encode('utf-8'),
                    "query": query
                    }
		try:
			cursor.execute('INSERT INTO Tweets VALUES (:id, :tweet_text, :query)',aux)
		except sqlite3.IntegrityError:
			pass

	conn.commit()
	conn.close()
	return ('', 204)


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8001))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)