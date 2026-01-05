# Simulacion Panel Solar

## Objetivo
modelar y analizar el comportamiento dinamico y electrico de un panel solar operando como fotodetector en un enlace de comunicaciones opticas por espacio libre (FSO), con el fin de determinar sus limitaciones en ancho de banda,  tiempo de respuesta, relacion señal a ruido y viabilidad para las señales moduladas

## Fundamento teorico
efecto fotoelectrico

## Metodologia
1. realizar una simulacion por medio de python para cumplir con el respectivo objetivo de la simulacion del panel solar

### Resultado

[Codigo SImulacion Panel Solar](../modelo/Panel_solar.py)

el primer modulo que es el de bloques constantes, nos expresa la sensibilidad, que se expuso en la simulacion anterior que es de -30 db, la responsividad que quiere decir que tanta eficiencia tiene el color rojo en el silicio, por cada Watt de luz genera aprox 0.4A, esa resistencia que se pondra en tu circuito, para lograr convertir la corriente en voltaje por medio de la ley de ohm, el bandwidth de 258kbps que fue hallado en el pwm_laser, gracias al Rise Time que se dio en el MOSFET, ademas la frecuencia de 5kHZ, del pin 9 del arduino que funciona el PWM
tenemos un modelado de capacitancia, ya que el panel funciona como un diodo gigante, porque permite que fluya la corriente en una sola direccion, evitando sobrecalentamientos, al ser tan grande, comparado con un fotoreceptor, funciona como un capacitor, se estima 1nanoFaradio por cada cm**2, ademas tenemos la frecuencia de corte que ela fomula de un filtro pasa bajos, y nos dice la frecuencia maxima antes de atenuarse, igual que hallamos el tiempo de subida
en el otro modulado hallamos la potencia tanto del margen mas la sensibilidad (-30db), y esa la multiplicamos por la responsividad dandonos de esta forma la corriente 
hallamos el ruido del sistema, tanto el ruido de Johnson (ruido por resistencia que genera calor), se calcula cuanto voltaje de ruido genera, ademas se halla el SNR entre la corriente y la resistencia, si el SNR>20 db la señal es nitida, pero si da menos de SNR <10 dB, y luego mada alerta si detecta un ancho de banda menor al esperado
igual que la fidelidad del sistema PWM, ya que el Rise Time es menor a los 200us (5kHZ)

---
2. Analisis de resultados

![Resultado 1](<Imagenes/Analisis 1.png>)
como primer instancia se agrega la medida del panel solar, se obtiene que con esta medida de 4cm2 nos brinda un BW de 39.79 Kbps, suficiente para transmitir de manera robusta sistemas de telemetria como en este caso SATs
ingresamos los valores del Margen de enlace en el canal_FSO en distancia de 100m, guardamos para cada fenomeno ambiental 

![Resultados 2 ](<Imagenes/Analisis 2.png>)
se observa que obtenemos una buena relacion señal a ruido, demostrando que tendremos buena fiabilidad de la señal, igual buena deteccion de corriente, igualmente como mencionamos anteriormente, a distacias cortas funciona casi de manera ideal, sin embargo, tenemos un ancho de banda bajo como se menciono anteriormente, el panel es lento para comunicar pero apropiado en las transmisiones de sistemas de alertas tempranas, ya que un fotodetector funciona de la siguiente manera es como un balde que se llena con un 1 y se vacia con un 0, pero un fotodiodo lo hace de manera muy rapida, sin embargo un panel solar es como una piscina olimpica, necesita muchos 1 y mucho tiempo para llenarla, y para vaciarla correspondientemente


## Conclusiones
la simulacion respalda el uso del panel solar como alternativa viable y de bajo costo para la recepcion optica en enlaces FSO de corta de distancia orientados a sistemas de alertas temprana. no obstante, para aplicaciones que requieran mayores tasa de datos o mayor alcance, seria necesario arquitecturas hibridas que separen la funcion de captacion de energia.