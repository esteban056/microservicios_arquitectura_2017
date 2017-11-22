# -*- coding: utf-8 -*-
from afinn import Afinn
import sqlite3
from flask import Flask, abort, render_template, request
import json
import os

afinn = Afinn(language = 'en')
app = Flask(__name__)




def analize(text):
	return 'positive' if afinn.score(text) > 0 else 'negative'

@app.route("/api/v3/sentiment", methods=['GET'])
def get_sentiment():
	query = request.args.get('t')
	conn = sqlite3.connect('tweets.db')
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	print cursor.fetchall()
	result = cursor.execute("SELECT * FROM Tweets WHERE query='"+query+"'")
	data = {}
	comments = []

	for row in result:
		data['id']=row[0]
		data['text']=row[1]
		data['query']= row[2]
		data['polarity'] = analize(row[1])
		comments.append(data)
		data = {}

	conn.close()
	return json.dumps(comments)

if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8002))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)