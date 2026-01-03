# Simulacion Canal_FSO

## Objetivo
modelar y evaluar el comportamiento del haz optico de 650nm al propagarse a traves de la atmosfera, atenuacion geometrica, fenomenos meteorlogicos y turbulencia, con el fin de lograr determinar la viabilidad del enalce y el margen de potencial disponible para una proxima recepcion

## Fundamento teorico
este fundamento esta regido, como se especifico en el marco teorico por la  UIT

### Metodologia

1. se plante el siguiente codigo en python 

## Resultados
[Codigo Simulacion FSO](../modelo/CANAL_FSO.py)

se plante las especificaciones del Hadware, tenemos una potencia de 5mW y la convertimos en decibeles obteniendo 6.99 dBm, la potencia minima requerida -30db ya que el panel solar no esta hecho como fotodetector, por esto debajo de esta potencia genera mucho ruido, con +7dBm es igual a 5.0mW
0dBm es igual a 1.0 mW, -10dbm es igual a 100uW, -20 dBm es igual a 10uW, y -30dbm es igual a 1uW,  del mismo modo se va usar un diodo laser de 650nm a 5mW, creamos una lista para ir guardando cada configuracion 
luego observamos un menu el cual nos da 3 opciones, crear un nuevo entorno, ver resultados y grafica o salir de la simulacion
en el caso de crear un nuevo entorno, aparece para ponerle un nombre que sera guardado a la lista de configuraciones, en este podemos escoger y dale valores a perdidas o escoger desde el nivel mas bajo, medio o alto, cada tipo de fenomeno, segun el fenomeno pide distintos valores, la distancia esta dada primordialmente un m, ademas intensidad de lluvia, nieve seca o humeda, etc, estas formulas fueron dadas en el marco teorico de la UIT,
por otro lado tenemos las turbulencia, que es creada por la turbulencia que es el viento o calor, la cual genera burbujas o eddy current, que afecta el canal de comunicacion, para esto damos 3 distintos niveles
igualmente se añadio perdidas por lentes, desalineacion y ventanas (fijo 5db)
cuando se hayan realizado o guardado todas las configuraciones, se puede guardar y seleccionamos la grafica, ahi seleccionamos una distancia, dando relacion de la distancia con las respectivas perdidas

---

2. se analiza la grafica de el enlace
 se obtiene una grafica comparativa entre las diferentes perdidas con 1000m y con 100 respectivamente
 ![Analisis de 1000m](<Imagenes/Grafica canal 1000m.png>)
 se observa que despues de los 300m las perdidas son exponenciales, igualmente por el efecto mile, se evidencia que la lluvia fuerte afecta drasticamente el enlace, igualmente la nieblina

 ![Analisis de 100m](<Imagenes/Grafica canal 100m.png>)
el panorama expresa que a los 100m tenemos un comportamiento casi ideal del enlace via FSO, y presenta el mismo comportamiento pero mas parejo entre las variables de perdida, ademas se observa que entro aprox los 5 primeros metros es casi constante, siendo optimo para la transmision

3. se analiza la tabla de resultados
 ![Analisis tabla 1000m](<Imagenes/Tabla resultado FSO.png>)
 como se habia observado el enlace falla ya que el valor de Margen es menor de 0 ya que nos dice cuanto es lo que necesitas, siendo mayor que 0 significa que esta mas arriba de lo que necesita, en este caso a 1000m significa que esta por debajo del margen 20 unidades de potencia, el respectivo panel solar no recibiria si no una pequeña parte

 ![Analisis tabla 100m](<Imagenes/Tabla resultado FSO 100.png>)
 en este caso se tienen en cuenta que esta 8 unidades arriba de lo que necesitamos, como se expuso anteriomente

 ### Observaciones
 hay que tener en cuenta que se configuro en las peores condiciones posibles, utilizando los mayores valores de dispesion 

## Conclusiones
finalmente las simulaciones permites concluir que el sitema FSO, propuesto es adecuado como desarrollo de proyecto ingenieril de investigacion, principalmente para distancias corta, si se desea tener escalar mas grandes se debe tener en cuenta el aumento de potencia del laser, la eleccion de la longitud de onda, la utilizacion de lentens colimados entre otros prototipos

