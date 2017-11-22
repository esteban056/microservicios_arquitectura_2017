# Arquitectura-Micro-Servicios
Repositorio de la tarea 2

## Sistema de Procesamiento de Comentarios

Antes de ejecutar el código asegurate de instalar los prerrequisitos del sistema ejecutando:
> sudo pip install -r requirements.txt  

Los paquetes que se instalarán son los siguientes:

Paquete | Versión                           | Descripción
--------|-----------------------------------|
Flask   | 0.10.1                            | Micro framework de desarrollo
requests| 2.12.4                            | API interna utilizada en Flask para trabajar con las peticiones hacia el servidor
afinn   |                                   | API para realizar analisis de sentimientos
tweepy  |https://github.com/tweepy/tweepy   | API Se recomienda usar la version de github porque las de algunos repositorios de linux estan desactualizados


*__Nota__: También puedes instalar éstos prerrequisitos manualmente ejecutando los siguientes comandos*   
> sudo pip install Flask==0.10.1  
> sudo pip install requests==2.12.4
> sudo pip install afinn
> sudo pip install -e git+https://github.com/tweepy/tweepy.git#egg=tweepy

Una vez instalados los prerrequisitos es momento de ejcutar el sistema siguiendo los siguientes pasos:  
1. Ejecutar el servicio:  
   > python servicios/sv_information.py  
   > python servicios/sv_tweets.py  
   > python servicios/sv_clasification.py  
1. Ejecutar el GUI:  
   > python gui.py  
1. Abrir el navegador
1. Acceder a la url del sistema:
   > http://localhost:8000/ - página de inicio!
# microservicios_arquitectura_2017

Las especificaciones de los servicios se encuentran en servicios/README.md
