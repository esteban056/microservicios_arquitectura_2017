# Servicios
En esta carpeta se define el servicio utilizado en la tarea 2 dentro del Sistema de Procesamiento de Comentarios (SPC). La especificación del servicio del Procesador de Comentarios de IMDb se realizó utilizando blueprint de Apiary.
La especificación es la siguiente:

## Procesador de Comentarios de IMDb
  
FORMAT: 1A  
HOST: https://uaz.cloud.tyk.io/content

## Information Service [/api/v1/information{?t}]

+ Parameters
    + t - Corresponde al título de la película o serie de Netflix.

### Get Information [GET]

+ Response 200 (application/json)

        { 
            "Title": "Some text",
            "Year": "Some text", 
            "Rated": "Some text",
            "Released": "Some text",
            "Runtime": "Some text",
            "Genre": "Some text",
            "Director": "Some text",
            "Writer": "Some text",
            "Actors": "Some text",
            "Plot": "Some text",
            "Language": "Some text",
            "Country": "Some text",
            "Awards": "Some text.",
            "Poster": "Some text",
            "Metascore": "Some text",
            "imdbRating": "Some text",
            "imdbVotes": "Some text",
            "imdbID": "Some text",
            "Type": "Some text",
            "totalSeasons": "Some text",
            "Response": "Some text"
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso: 
1. Abrir el navegador
1. Ingresar a https://uaz.cloud.tyk.io/content/api/v1/information?t=Stranger+Things

FORMAT: 1A
HOST: http://localhost:8002/

# Clasification

Clasification es una API que permite obtener el texto de tweets guardados en la base de datos y
los clasifica en polaridad positiva o negativa de acuerdo a su contenido
## Clasificador de comentarios de twitter [/api/v3/sentiment{?t}]

### Get Sentiment [GET]
+ Parameters:
    + t (String) Nombre de la pelicula para buscar comentarios relevantes
+ Response 200 (application/json)

        [
            {
                "polarity": ("positive "|"negative"), 
                "text": "comment", 
                "username": "twitter username", 
                "id": "933177335632687109", 
                "query": "twin peaks"
            }, 
            {
                "polarity": ("positive "|"negative"), 
                "text": "comment", 
                "username": "twitter username", 
                "id": "933177203495456768", 
                "query": "twin peaks"
            }, 
            {
                "polarity": ("positive "|"negative"), 
                "text": "comment", 
                "username": "twitter username", 
                "id": "933175901121998850", 
                "query": "twin peaks"
            } 
            
        ]

FORMAT: 1A
HOST: http://localhost:8001/

# Tweets

Tweets es una api simple para pedir comentarios de twitter relevantes a una pelicula o serie de television, y los guarda en una base de datos

## Recolector de comentarios de twitter [/api/v2/tweets?{?t}]

### Get Tweets  [GET]
+ Parameters:
    + t (String) nombre de la pelicula a buscar
    
+ Response 204 