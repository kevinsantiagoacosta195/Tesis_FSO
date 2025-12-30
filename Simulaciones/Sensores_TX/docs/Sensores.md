Fecha: 21/12/2025
# Simulación de Sensores SATs

## Objetivo
se describe el funcionamiento entre el sistema de alerta tempra y el MCU, permitiendo verificar el correcto funcionamiento del conjunto de sensores, permitiendo asi validar los datos en ambitos ideales, obteniendo asi una mayor fiabilidad en los datos que se registran

## Fundamento Teórico
 uso de sensores para identificar desastres natuales o desastres producidos por el ser humano, para ello hacemo uso de un sensor MQ-2 que permite detectar la presencia relatia de gases inflamables mediante la variacion de su resistencia interna, la cual la traduce en voltaje proporcional. Por otro lado el sensor BME280, permite medir la temperatura, humedad y presion atmosferica mediante sensores microelectronicos integrados, cuyas variaciones son convertidas a datos digitales, que permiten monitoreo ambiental y control del sistema, por ultimo, el modulo HCSR04 permite determinar la distancia a un objeto mediante la emision de pulsos ultrasonicos y medicion real del eco reflejado, es muy util para calcular la distancia en funcion de la velocidad del sonido, por esto es fundamental, para medir inundaciones, cabe recalcar que se desea implementar un sensor mas para medir sismos, este es el ADXL345, encargado de medir la aceleracion y vibracion, pero este no se tomara en cuenta para la respectiva simulacion, ya que no se encuentra dentro del software de simulacion

## Metodología

Pasos de la simulación:
1. descargar el software de simulacion (proteus 8)
2.  Realizar un sistema de prueba para validar el enlace entre proteus y arduino
--- para esto se hace uso de un sistema que cuenta con arduino, led, boton y resistencia

### Resultados
![Proof of Concept](<Imagenes/Esquematico, Prueba.png>)
**Figura 1:** como se puede observar en esta figura representa un esquematico que se realiza en proteus, la finalidad de este ejercicio es poder realizar una validacion de un enlace entre arduino y proteus, en este caso, se hace uso de un arduino uno, un boton, un led color verde, una resistencia de 10k, una resistencia de 220 ohminios, su finalidad es pulsar el boton y despues de esta accion se enciende el boton el tiempo que se halla programado en Arduino IDE, en este caso 5 segundos

[Codigo arduion, PoC](<../modelo/PRUEBA VINCULO/Vinculo_Proteus_Arduino/Vinculo_Proteus_Arduino.ino>)
**codigo 1:** esto codigo, se basa primero en la asignacion de pines tanto para el led como para el boton, se crea un condicional, en el caso que se oprime el boton el led se mantiene encendido 5 seg cuando no esta presionado, el led se mantiene "LOW"

### Observaciones
se observa el correcto funcionamiento de la simulacion obteniendo el resultado esperado ya que se realizo con el fin de probar la correcta iteraccion entre el Arduino y proteus, permitiendo la escalabilidad en los proximos proyectos, partiendo desde la comprobacion de ideas

3. implementar el sensor HCSR04, el cual es el encargado de medir el nivel de agua en el proyecto, para evitar futuras inundaciones o salvaguardar la vida de las personas que se encuentran por eso se realizo su respectiva simulacion en proteus
--- por esto se implemento un arduino UNO, un sensor HCSR04, un led y una resistencia de 220 ohmnios

### Resultados
![Simulacion HCSR04- Apagado](<Imagenes/Esquematico HCSR04- Apagado.png>)
**Figura 2**: en este esquematico se evidencia la implementacion de un arduino Uno, el cual permite controlar y analizar el sensor HCSR04, por medio del pin Tr que es aquel que permite que inicie a funcionar el sensor, en este caso el MCU, le avisa que cuando reciba un pulso de 10 microsegundos debe empezar a trabajar (envia 8 rafagas de ultrasonido), este va conectado al pin 3, mientra por otro lado el pin ECHO, menciona cuanto tiempo se demoro el sonido en rebotar y regresar, ademas cuenta con un led color rojo que permite avisar cuando un objeto, fenomeno, etc esta a una distancia determinada en este caso a los 15 cm no se activa la alrma

![Simulacion HCSR04- Encendido](<Imagenes/Esquematico HCSR04- Encendido.png>)
**Figura 3**: como se menciona en la parte anterior cuando el sensor identifica un objeto a una distancia determinada lanza la alarma, es importante añadir, que dentro de la simulacion de proteus, se imprime un mensaje en el serial del simulador especificando los valores


[Codigo HCSR04](../modelo/SENSORE_COMPLETED/HCSR04/Sensores_Tesis_HCSR04/Sensores_Tesis_HCSR04.ino)
este codigo especifica el umbral critico el cual nosotros considiremos de peligro, indicamos los pines del sistema, especificamos del mismo modo el disparo del sensor (Trig), tambien especificamos la que esta dada por, distancia = duracion * 0.034 / 2; como se sabe la velocidad del sonido es de 343 m/s, en este caso estamos usando microsegundos y cm, por lo cual su conversion nos da un resultado de 0,034, mientras que el 2 hace referencia a la ida y la vuelta del sonido.

### Observacion
la simulacion y el cambio de parametros se realiza de manera manual, por lo cual no se relaciona con el evento real, sin embargo se esta diseñando la logica y estructura del sistema
del mismo modo en primer instancia en la simulacion del sensor mq-2, ocupaba mucha CPU, por lo cual se guio 

---

## Fecha: 22/12/2025
4. se realiza la respectiva simulacion del sensor MQ-2, encargado de medir la variacion de gases en Protus 8

## Observaciones
el MQ-2 que se encuentra en el proteus, pero se encuentra muy inestable y pretende a evidenciar fallos como se evidencia en la siguiente imagen
"Unable to open HEX file '..\..\..\..\..\..\..\..\..\..\..\..\..\Program Files (x86)\Labcenter Electronics\Proteus 8 Professional\DATA\GasSensorTEP.HEX'. [GAS1]"
esto se deduce que pasa por el documento .hex de la libreria gas, no permite ejecutar me manera correcta el modulo electronico dentro del programa

![Error MQ-2](<Imagenes/Error MQ-2.png>)
**Figura 4** se evidencia el esquema electronico, en donde se hace uso de un Arduino UNO, un MQ-2, un led, resistenca de 220 ohmnios, Un potenciometro, y ademas cuenta con un virtual terminal encargado de leer los valors, se presenta esta figura como comprobacion de simulacion

---

## Fecha: 22/12/2025
5. como solucion al anterior problema, se pretende simular el sensor MQ-2, por medio de un potenciometro mostrando el cambio que se presentaria en un gas en la vida real
--- por esto se plantea un esquema electronico con un Arduino UNO, LCD, POT-HG (Potenciometro),Ground y Power

### Resultados
![Simulacion MQ-2](<Imagenes/Sensor MQ-2, Sin Gas.png>)
**Figura 5** se evidencia que la pantalla LCD, enseña un mensaje anunciando, si hay algun tipo de fuga, en este caso no existe algun tipo de fuga, ya que el valor se encuentra en un valor menor a 0.7, que se puso como valor de calidad de aire satisfactoria.

![Simulacion MQ-2, con Fuga](<Imagenes/Sensor MQ-2, con Gas.png>)
**Figura 6** se evidencia que la pantalla LCD, enseña un mensaje anunciando, si hay algun tipo de fuga, en este caso si se detecta gas, esto principalmente porque su valor esta por encima de 0.7, señalando mala calidad de aire, en donde puede existir algun gas que es daniño para la humanida

Referencia: https://www.google.com/search?q=simulacion+proteus+arduino+mq2&oq=simulacion+proteus+arduino+mq2&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRiPAjIHCAQQIRiPAtIBCDY5MjRqMGo3qAIIsAIB8QVF-us5UustZ_EFRfrrOVLrLWc&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:f1fe69e9,vid:BMW7e94QL_I,st:0

[Codigo MQ-2](../modelo/SENSORE_COMPLETED/MQ-2/MQ-2/MQ-2.ino)
temas que se deben resaltar en este codigo es la conversion del valor del ADC del arduino a voltaje, esto con el fin de definir el valor concreto del gas, ya que el arduino tiene un ADC de 10 bits que lo que hace es convertir un valor analogico a digital, cuando hace esto declara una condicional, el cual, si el valor de el voltaje es menor a 0,70 no se ha detectado gas, pero por el contrario, si el valor es mayo a 0,70 se ha detectado algun gas
referencia: https://www.youtube.com/watch?v=747xqP4OCiw

###  Observaciones
se observa en este caso la falla del modulo directamente de la aplicacion, y se reitera que el cambio se debe hacer manual, el usuario es el que modifica el valor esperado, pero permite comprobar el funcionamiento de tanto el software como el hadware del sistema

6. para finalizar el conjunto de sensores individuales, se procede hacer la simulacion del sensor BME280
--- para esto se hace uso de un Arduino Uno, un sensor BME280, tres leds como sistema de alerta, tres resistencias de 220 ohmnions

### Resultados
![BME280 SIMULACION](<Imagenes/BME280 Apagado.png>)
**figura 7** como se observa en la figura de la simulacion, contamos con un bme280 el cual nos indica principalmente, tres variables (Temperatura, Humedad y presion atmosferica), en esta figura se observa que todos los leds estan apagados, quiere decir que ningun valor esta anormal, en el caso de la temperatura se encuentra menor a 30 grado centigrados, mientras que la humedad ambiente tambien en menor de 60%, y por su parte la presion atmosferica no es menor de 1000 hpa, esto es porque si se baja la presion atmosferica de manera inusual puede ser razon de tormenta, o gran cantidad de lluvia (referencia: https://www.clima.com/meteopedia/baja-presion-atmosferica )

![BME280 ALARMA TEMPERATURA](<Imagenes/BME280- ALARMA TEMP.png>)
**figura 8** como se menciono anteriormente las alarmas se activan en el momento que las variables toman valores distintos a los señalados en la programacion, en este caso la temperatura es mayor de 30 grados centigrados, especificamente 31 grados centigrados.

![BME280 ALARMA HUMEDAD](<Imagenes/BME280- ALARMA HUME.png>)
**figura 9** como se menciono anteriormente las alarmas se activan en el momento que las variables pasan su valor umbral, en este caso la humedad es mayor de 60% Hr , especificamente 61% Hr.

![BME280 ALARMA ATM](<Imagenes/BME280 - ALARMA ATM.png>)
**figura 10** como se menciono anteriormente las alarmas se activan en el momento que las variables pasan o disminuyen su valor umbral, en este caso la atmosfera es redujo su hpa, arrojando un valor de 980 hpa

[CODIGO BME280](../modelo/SENSORE_COMPLETED/BME280/BME280_Ard/BME280_Ard.ino)
cabe destacar, que fue necesario la carpeta "Adafruit_BME280.h", asociada al sensor BME280, como primera intancia, declaramos los pines referente a los leds. asi mismo señalamos los valores de los umbrales, se inicializa el BME280, se leen las variables de temperatura, humedad y presion atmosferica (la Presion se divine en 100 ya que pasamos de Pa "Pascales" a hpa "hectopascales"), muestra los datos, y al final los compara con el valor umbral, para lanzar la advertencia.

### Observaciones
No se hacen observaciones referente a esta simulacion 

7. para finalizar la simulacion de los sensores SATs, se realizo una simulacion integrando los tres esquematicos anteriores (HCSR04, MQ-2 y BME280), implementando su sistema de alerta por medio de leds
--- para esto se hizo uso de un Arduino uno , sensor HCSR04, LCD, 4 Leds, 4 resistencia 220 ohminios, BME280, potenciometro POT-HG

### Resultados
![Sistema de Sensores Completo](<Imagenes/SATs Tesis.png>)
**Figura 10** en el esquematico final se evidencia, la union entre los tres sistemas como se menciono anteriormente, algo a resaltar es el uso de la pantalla LCD, para informar acerca de los tres sensores, ademas la manera de distribucion de los pines del Arduino, tambien es algo a resaltar, 

[Codigo Sistema de Sensor Arrays](<../modelo/PROYECTO SAT FINALIZADO/SENSORES_ARD/SENSORES_ARD.ino>)
dentro del codigo se da por primera instancia los pines de el Lcd, el BME280, el POT-HG, y los leds, luego señalamos los valores de umbral de nuestro sistema, en donde ya sea mayor o menor el valor, saltara la alarma, inicializamos los parametros, realizamos las comparaciones de los valores que recibimos, referente a los valores de umbral, e imprimimos los datos en la pantalla LCD

---

## Fecha: 24/12/2025

## Conclusiones
- se logro implementar de manera exitosa la simulacion tanto individual, como conjunta del sistema de sensores SATs mediante el software Proteus 8, permitiendo validar la logica de funcionamiento del sistema de alerta temprana antes de su implementacion fisica
 - del mismo modo permitio validar la comunicacion entre el MCU y los sensores, garantizando lectura, procesamiento y visualizacion de las variables de ambiente y riesgo
 - se realizo un optimo enlace entre ambas aplicaciones, permitiendo la prueba del codigo, gracias al IDE de Arduino, asi como la implementacion del hadware en Proteus 8
 - el uso de indicadores visuales como los LEDs y la pantalla LCD facilito la interpretacion del estado del sistema, mejorando la comprension del comportamiento de cada sensor y el conjunto de estos

## Recomendaciones
- implementar la simulacion varios sensores que no fueron posibles de añadir, como el mq-2, el ADXL345.
- implementar serie de datos segun regiones para la lectura de los sensores, ya que se tenia que probar de manera manual, con lo cual, no funcionaba de manera automatica segun su entorno, permitiendo desarrollar un registro de datos, para el analisis historico de eventos asi como la respectiva comparacion con el hadware real, ademas como no es posible hacerlo de esta manera en proteus 8, no fue posible la implementacion de un sistema de filtrado y promediado para reducir el ruido de las mediciones
- cabe mencionar que los sensores en el proyecto simplemente generan los datos, no son precisamente el aporte cientifico, por lo cual su importancia es valida, pero no fundamental
