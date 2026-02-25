## FECHA: 21/12/2025
**Fase:** Inicio del Proyecto (Desarrollo Prototipo)
**Tiempo Dedicado:** 20 minutos

## Objetivo:
Se inicializa formalmente el desarrollo del proyecto de tesis (Sistema FSO, haciendo uso de paneles solares como fotoderectores, para la transmision y detencion de Sistemas de Alertas Tempranas), para asi poder establecer un sistema organizado de documentacion y control en la respectiva elaboracion

## Fundamento
La trazabilidad y el registro es parte fundamental, para medir la respectiva evolucion del proyecto, asi como el desarrollo experimental del proyecto

## Actividades realizadas 
1. Creacion de repositorio para la documentacion de la tesis
2. Definicion de la estratehia del trabajo incremental
3. decision de documentar el proceso mediante una bitacora tecnica (Notion)
4. Sincronizacion del repositorio con GitHub

## Resultado
Creacion organizada de repositorio (Bitacora) para medir el avance

## Decision de Ingenieria
se adopta GitHub como herramienta principal de trazabilidad del proyecto

## Observaciones
se implementa carpetas en el repositorio segun se va avanzando con el desarrollo

## Proximo paso
Iniciar la fase de diseño conceptual del sistema

---

## FECHA: 21/12/2025
**Fase:** Diseño conceptual
**Tiempo Dedicado:** 1 hora

## Objetivo
definir la arquitectura General del sistema de comunicacion optica por espacio libre (FSO), la cual, se presenta en el documento en el apartado de diseño metodologico.

## Fundamento
Modelo basico e inicial de un enlace optico en sistemas de alertas tempranas, permitiendo desglozar bloque por bloque para su posterior implementacion y analisis.

## Actividades Realizadas
1. Identificacion de los bloques funcionales del sistema
2. Analisis de los subsistemas de transmision y receptor

## Resultados
se realizo la arquitectura del sistema de bloques, en terminos tanto generales como especificos, dando referencia asi a la conceptualizacion de los subsitemas del proyecto

### Diagrama de bloques

 **Diagrama de bloques General**
 ![Diagrama de bloques general](<Diagramas de flujo/Diagrama de flujo AC.png>)
 **Figura 1.** Diagrama de bloques correspondiente a la señal AC, en el cual
se representa la transmisión de la información proveniente de los sensores
hasta el panel solar a través de un enlace FSO.

 ![Diagram de bloque general](<Diagramas de flujo/Diagrama de flujo DC.png>)
**Figura 2.** Diagrama de bloques correspondiente a la señal DC, el cual
representa el aprovechamiento energético del sistema para la alimentación
de la etapa de alarma.

 **Diagrama de bloques especifico**
 ![Diagrama de bloque especifico](<Diagramas de flujo/Diagrama de flujo General.png>)
Diagrama de bloques del diseño técnico del sistema de
comunicación óptica FSO, utilizando paneles solares como fotodetectores
para la transmisión y recepción de señales asociadas a sistemas de alerta
temprana (SAT).

## Observaciones 
Aún no se han definido los valores numéricos de las variables del sistema.
Los elementos presentados tanto en el documento como en los diagramas
están sujetos a pruebas experimentales y posibles modificaciones durante
el desarrollo del proyecto.

## Proximo paso
Iniciar la fase de simulaciones del sistema

---

## FECHA: 21/12/2025
**Fase:** Elaboracion de Simuaciones
**Tiempo Dedicado:** 1 hora

## Objetivo
implementar el sistema de comunicacion optica por espacio libre (FSO), mediante herramientas de simulacion, con el fin de idealizar el comportamiento del sistema y analizar su diseño preeliminar

## Fundamento
la implementacion de simulaciones, es fundamental para comprender el comportamiento optico de un sistema antes de su realizacion fisica (Prototipo). en esta caso se simula un enlace FSO que emplea paneles solares como elementos de fotodeteccion

## Actividades Realizadas
1. Planeacion de la estrategia de simulacion del sistema
2. definicion de los bloques a simular de forma individual
3. identificacion de variables y parametros inicialess

## Resultados
se establece el enfoque de simulacion del sistema, organizacion, planteamiento, definiendo asi su orden y alcance de cada uno de los bloques a modelar

## Observaciones 
Aun no se ha definido valores numericos especificos, que serian establecido en futuroas instancias, por medio, del uso de la simulacion individual de cada bloque

## Proximo paso
Simulacion sensores de los sistemas de alerta temprana  junto al MCU

---

## Fecha: 21-12-2025
**Fase:** Simulación  
**Bloque:** Sensores de los SATs en el bloque TX
**Tiempo Dedicado:**

## Objetivo
modelar el comportamiento de los sensores asociados a los sistemas de alerta tremprana, y su respectiva interaccion con el bloque de transmision, permitiendo generar control, analisis y su respectiva alerta, para eso es importante escoger sensores que permitan representar distintos desatres tanto naturales, como aquellos que interviene el ser humano

## Fundamento
en esta etapa de diseño y simulacion, los sensores pueden ser representados mediante modelos ideales, lo que permite analisar su comportamiento temporal, esta aproximacion permite evaluar la generacion de datos sin perdida y con buena fiabilidad

## Decision
se hara uso de el software de simulacion Proteus 8 professional, permitiendo representar tanto componentes electronicos, si no tambien permite el analisis de señales

## Actividad Realizadas
1. instalacion de Proteus 8
2. uso de un MCU de arduino (Arduino Uno) 
3. Enlace entre proteus y arduino realizando un sistema de verificacion por medio de un led, creando un Poc (Proof of Concept)
4. Implementacion del sensor HCSR04 el cual permite medir el nivel del agua que experimenta el sistema, usando un led para activar el sistema de alerta

[Para mayor Especificaciones, ingresar al siguiente link: ](../Simulaciones/Sensores_TX/docs/Sensores.md)
## Resultado
se evidencia en caso del HCSR04, con el respectivo cambio manual de las varibale se evidencia la efectividad del sistema

## Observaciones
El ESP32 no esta dentro del modelo de proteus, por lo cual se hace uso del arduino Uno para comprobar la logica del sistema

---

## Fecha: 2025-12-22
**Fase:** Simulación  
**Bloque:** Sensores de los SATs en el bloque TX
**Tiempo Dedicado:**

## Objetivo
continuar con el proceso de simulacion de los sensores del sistema de alertas tempranas, permitiendo comprobar la logica, y facilitar del mismo modo la futura implementacion en el prototipo

## Fundamento
en esta etapa de diseño y simulacion, se probara el funcionamiento de sensores tales como el mq-2, encargado de medir los niveles de toxicidad del aire, ademas probar el sensor bme280, encargado de medir la humedad, temperatura, y presion atmosferica, para asi integrar el sistema completo

## Decision
se hara uso de el software de simulacion Proteus 8 professional y Arduino IDE, permitiendo representar tanto componentes electronicos, si no tambien permite el analisis de señales

## Actividad Realizadas
1. Realizar la simulacion de el sensor MQ-2 encargado del medir el nivel de toxicidad del aire
[Para mayor Especificaciones, ingresar al siguiente link: ](../Simulaciones/Sensores_TX/docs/Sensores.md)

## Observaciones
el MQ-2 que se encuentra en el proteus, pero se encuentra muy inestable y pretende a evidenciar fallos como se evidencia en la siguiente imagen

"Unable to open HEX file '..\..\..\..\..\..\..\..\..\..\..\..\..\Program Files (x86)\Labcenter Electronics\Proteus 8 Professional\DATA\GasSensorTEP.HEX'. [GAS1]"

![MQ-2 Error](<../Simulaciones/Sensores_TX/docs/Imagenes/Error MQ-2.png>)

esto se deduce que pasa por el documento .hex de la libreria gas 

## Decision
se simula el sensor MQ-2, por medio de un potenciometro mostrando el cambio que se presentaria en un gas en la vida real

---

## Fecha: 2025-12-23
**Fase:** Simulación  
**Bloque:** Sensores de los SATs en el bloque TX 
**Tiempo Dedicado:**

## Objetivo
continuar con el proceso de simulacion de los sensores del sistema de alertas tempranas, permitiendo comprobar la logica, y facilitar del mismo modo la futura implementacion en el prototipo

## Fundamento
en esta etapa de diseño y simulacion, se probara el funcionamiento de sensores tales como el mq-2, encargado de medir los niveles de toxicidad del aire, ademas probar el sensor bme280, encargado de medir la humedad, temperatura, y presion atmosferica, para asi integrar el sistema completo

## Decision
se hara uso de el software de simulacion Proteus 8 professional y Arduino IDE, permitiendo representar tanto componentes electronicos, si no tambien permite el analisis de señales

## Actividad Realizadas
1. se implmenta una pantalla LCD en proteus
2. se implementa un arduino UNO
3. se enlaza proteus con el codigo de arduino
4. se agrega el potenciometro
5. se completa la simulacion
6. se observa el cambio de valor y su respectiva alarma
7. se inicia la implementacion del sensor Bme280, como ultimo sensor en el bloque de simulaciones, para asi hacer prueba del conjunto completo
8. se añade el MCU
9. se implementa leds de alarma y el sensor Bme280
10. se realiza la simulacion (Cambiando valores manualmente)
11. se acopla todos los 3 sensores, utilizando un mismo MCU.
12. se utiliza led, como sistema de alarma.
13. se utiliza una pantalla para visualizacion de datos.


[Para mayor Especificaciones, ingresar al siguiente link: ](../Simulaciones/Sensores_TX/docs/Sensores.md)

## Observaciones
se cambio el valor del potenciometro POT-HG, de manera manual, asemejando el sensor MQ-2 como se menciono anteriormente se cambio haciendo referencia al sensor 

---

## Fecha: 2025-12-26
**Fase:** Simulación  
**Bloque:** Transmisor Optico (PWM_LASER)
**Tiempo Dedicado:**

## Objetivo
Demostrar como una señal digital generado por un MCU, puede modular opticamente un laser via PWM, produciendo una potencia optica proporcional a la informacion que luego viaja en el canal FSO

## Fundamento
es fundamental comprender como se comporta el transmisor optico, para asi ser capaz de transmitir informacion por medio de un laser, con una modulacion PWM, del mismo modo, comparar los datos en un contexto ideal, como es en una simulacion, y en entorno real

## Decision
se hara uso de el software de simulacion Proteus 8 professional y Arduino IDE, permitiendo representar tanto componentes electronicos, si no tambien permite el analisis de señales

## Actividad Realizadas
1. montar un MCU (Arduino Uno)
2. una resistencia 1k
3. transistor 2N2222 NPN
4. en el emisor una resistencia de 10 ohmion  encargada de medir la corriente por medio del osciloscopio, por lo cual se utiliza la ley de ohm para poder tener valores lo mas aproximados posibles
5. un LED-ROJO, que funciona como el laser, controlando por medio de la corriente la potencia optica
6. resistencia 220 permite que no se queme el led
7. se vincula Arduino con proteus
8. se realiza analisis de señales, voltaje en el pin 9 y voltaje en la resistencia Shunt
9. se descarga los datos de las graficas Duty 0, 25, 50, 75, 100
10. se analiza por medio de Python, y se analiza

[Para mayor Especificaciones, ingresar al siguiente link:](../Simulaciones/Pwm_Laser/docs/Pwm_Laser.md)


## Observaciones
se observa que la señal, no representa la ideal, concluyendo que se presentan perdidas principalmente entre el Duty 25 y el 75, princialmente por el transistor BJT, 2N2222, ya que no conmuta de manera eficaz y rapida, se busca una respectiva alternativa.

---

## Fecha: 2025-12-29/30
**Fase:** Simulación  
**Bloque:** Transmisor Optico (PWM_LASER)
**Tiempo Dedicado:**

## Objetivo
Desarrollar un modelo eficaz, estable e ideal, que genere una señal PWM, para lograr la transmision efectiva de SATs, ademas que permita simular de manera efectiva su comportamiento

## Fundamento
es fundamental comprender como se comporta el transmisor optico, por medio de un transistor MOSFET, capaz de conmutar de manera rapida y eficaz, permitiendo generar una señal PWM, estable y sin demasiada perdidas

## Decision
se hara uso de el software de simulacion Proteus 8 professional y Arduino IDE, permitiendo representar tanto componentes electronicos, si no tambien permite el analisis de señales, usando MOSFETs

## Actividad Realizadas
1. montar un MCU (Arduino Uno)
2. una resistencia 220
3. Resistencia 10K, para evitar que el MOSFET cuando el MCU, este con alta impedancia, ademas reducir el efecto Miller
3. transistor MOSFET
5. un LED-ROJO, que funciona como el laser, controlando por medio de la corriente la potencia optica
6. resistencia 220 permite que no se queme el led
7. un condensador snubber con una recistencia para disipar
8. usar un graphics analogue, para simular el comportamiento de la señal pwm producida
9. exportar los datos a un archivo .DAT
10. analizarlos con python, hallando parametros tales como la frecuencia, el Duty que se evidencia en la grafica, el error DC, Rise Time y el Bandwitdh del sistema

[Para mayor Especificaciones, ingresar al siguiente link:](../Simulaciones/Pwm_Laser/docs/Pwm_Laser.md)

### Observaciones
N/A

## Fecha: 02/1/2026
**Fase:** Simulación  
**Bloque:** Canal Optico
**Tiempo Dedicado:**

## Objetivo
Simular el funcionamiento conceptual del canal FSO, en el cual se transmitira por medio de un laser, previamente simulado, analizando de esta forma las perdidas y la respectiva potencia del canal FSO

## Fundamento
es fundamental comprender como se comporta el Canal par observar como el canal optico, permita que la informacion viaje de manera efectiva al panel solar, logrando asi demodular la informacion, esto se realizara teniendo en cuanta la potencia reglamentaria, las perdidas atmosfericas, por centelleo, etc

## Decision
se hara uso de el software de simulacion Por proteus, en donde permite el analisis de las perdidas en el canal, asi como la implementacion de formulas previamente especificadas en el marco teorico.

## Actividad Realizadas
1. hacer uso del lenguaje de programacion python para realizar las respectivas ecuaciones presentadas por la ITU
2. analizar las graficas que se presentaron tanto el comportamiento de las señales como su tablas de resultados

[Simulacion canal FSO](../Simulaciones/Canal_FSO/docs/Canal_FSO.md)

### Observaciones
hay que tener en cuenta que la distancia a la que se va a realizar es casi ideal, ya que el prototipo es de entre 1 a 2 metros por mucho

---

## Fecha: 03/01/2026
**Fase:** Simulación  
**Bloque:** Panel solar como Fotodetector
**Tiempo Dedicado:**

## Objetivo:
simular y analizar el comportamiento del panel solar como fotodetector, observando asi su efectividad en temas de velocidad para lograr demodular la señal PWM, mandad por el laser de 650nm, de igual manera mirar su SNR, sus limitaciones fisicas

## Fundamento
con esta simulacion permitira comprobar, el funcionamiento teorico del panel solar como fotodetector, de igual manera permitiria, simular en siguientes instacias, temas como el filtrado, la potencia, y la decodificacion de la informacion

## Desicion
realizar una simulacion por medio de Python, en donde se use teorica para simular el comportamiento del panel solar como fotodetector

## Actividades Realizadas
1. realizar el codigo sobre la simulacion del panel solar

2. analisis de los datos proporcionados por el programa

[Simulacion FSO](../Simulaciones/Panel_Solar_RX/docs/Panel_Solar.md)

## Observaciones 
se observa que el panel solar no permite transmision de alta velocidad, sin embargo apropiada para comunicacion de SATs.

---

## Fecha: 05/01/2026
**Fase:** Simulación  
**Bloque:** Panel solar y circuito Bias-T, filtrado
**Tiempo Dedicado:**

## Objetivo:
simular y analizar el comportamiento del panel solar como fotodetector, asi mismo simular el circuito Bias-T, en donde dividimos la informacion, y la respectiva informacion, con el fin de permitir que llegue de manera efectiva la informacion.

## Fundamento
con esta simulacion se puede interpretar de manera efectiva, la manera en la que es posible extraer la informacion de manera integra, asi como se puede aprovechar el sistema de energia para poder alimentar alarmas o entre otros dispositivos electronicos

## Desicion
realizar una simulacion por medio de python y de proteus.

## Actividades Realizadas
1. realizar el codigo sobre la simulacion del panel solar y el circuito bias-t, por medio de python

2. analisis de los datos proporcionados por el programa


[Simulacion Bias_t](../Simulaciones/Bias_T_Filtros/docs/BiaS_T.md)

## Observaciones 
No se pudo realiza la simulacion por varias pruebas ya que se estaba aprendiendo la manera correcta en utilizar el LM328N como tanto amplificador, y comparador 

---

## Fecha: 08/01/2026
**Fase:** Simulación  
**Bloque:** Panel solar y circuito Bias-T, filtrado
**Tiempo Dedicado:**

## Objetivo:
simular y analizar el comportamiento del panel solar como fotodetector, asi mismo simular el circuito Bias-T, en donde dividimos la informacion, y la respectiva informacion, con el fin de permitir que llegue de manera efectiva la informacion.

## Fundamento
con esta simulacion se puede interpretar de manera efectiva, la manera en la que es posible extraer la informacion de manera integra, asi como se puede aprovechar el sistema de energia para poder alimentar alarmas o entre otros dispositivos electronicos

## Desicion
realizar una simulacion por medio de python y proteus.

## Actividades Realizadas
1. realizar el codigo sobre la simulacion del panel solar y el circuito bias-t, por medio de python
2. analisis de los datos proporcionados por el programa
3. realizar el circuito bias tee, usando la idealizacion de un panel solar, igualmente, plantear el respectivo circuito Bias Tee, ademas realizar la etapa de amplificacion y digitalizacion
4. hacer analisis de el comportamiento de la señal


[Simulacion Bias_t](../Simulaciones/Bias_T_Filtros/docs/BiaS_T.md)

## Observaciones 

---

## Fecha: 09/01/2026
**Fase:** Prototipado real
**Bloque** PWM_LASER

## Objetivo:
realizar el prototipo del funcionamiento del laser con el transistor MOSFET, igualmente la implementacion de PWM, para la respectiva modulacion de la informacion

 ## Metodologia
 1. usamos el modulo Mosfet LR7843, soldamos los respectivos pines
 ![MODULO LR7843 SUPERIOR](<Imagenes Prototipo/09_01_2026/MODULO MOSFET SUP.jpeg>)
 ![MODULO LR7843 INFERIOR](<Imagenes Prototipo/09_01_2026/MODULO MOSFET INF.jpeg>)
 2. conectamos el arduino pin 9 al pwm del modulo y gnd con gnd
 ![CONEXION ARUINO](<Imagenes Prototipo/09_01_2026/ARDUINO MOSFET.jpeg>)
 3. probamos que la fuente tenga 5V
 ![COMPROBAR 5V](<Imagenes Prototipo/09_01_2026/PRUEBA FUENTE.jpeg>)
 4. conectamos el positivo del laser y el positivo de la fuente al + del modulo
 ![CONEXION POSITIVOS TANTO FUENTE COMO LASER](<Imagenes Prototipo/09_01_2026/LASER +, + FUENTE MOSFET.jpeg>)
 5. conectamos el negativo del laser al load del arduino
 ![GND LASER](<Imagenes Prototipo/09_01_2026/MOSFET - LASER.jpeg>)
 6. conectamos el negativo de la fuente al - del modulo
 ![GND FUENTE](<Imagenes Prototipo/09_01_2026/MOSFET - FUENTE.jpeg>)
 7. montamos el codigo de la simulacion PWM
 [Codigo Simulacion PWM](../Simulaciones/Pwm_Laser/modelo/ARD__PWM_LASER/ARD__PWM_LASER.ino)
 8. probamos simulacion de modulacion OOK
 <video controls src="Videos Prototipo/09_01_2026/OOK LASER.mp4" title="Simulacion OOK"></video>
 8. probamos varios 5KHZ PWM
 <video controls src="Videos Prototipo/09_01_2026/PWM 5KHZ.mp4" title="PWM 5kHz"></video>

### Observaciones 
se observa que el brillo del led no cambia ya que el ojo humano no detencta estas variaciones tan rapidas de 5khz, igualmente toco cambia de arduino uno ponque el pin 9 no entregaba el voltaje suficiento, teniendo como resultado que el laser no se prendiera, sin embargo a la hora de cambiar funciono de manera correcta. de la misma forma se debe implementar el mismo sistema con un laser de punto en cambio de el laser de cruz

---

## Fecha: 10/01/2026
**Fase:** Prototipado Real
**Bloque:** Panel solar, Bias TEE

## Objetivo:
realizar el circuito Bias T e implementarlo junto al panel solar para hacer el respectivo SWIPT, de igual maneja dejar listo ambos bloques para lograr en otra ocasion unificar la comunicacion.

## Metodologia:
 1. soldamos tanto cable rojo (+), como negro (-) al panel solar
 ![SOLDADA + PANEL](<Imagenes Prototipo/10_01_2026/SOL_PANEL_+.jpeg>)
 ![SOLDADA - PANEL](<Imagenes Prototipo/10_01_2026/SOL_PANEL_-.jpeg>)

 2. soldamos del filamento de los cables mencionados anteriormente a un jumper para poder asi usarlo en la protoboard
 ![UNION + PANEL JUMPER](<Imagenes Prototipo/10_01_2026/UNION_+_+.jpeg>)
 ![UNION - PANEL JUMPER](<Imagenes Prototipo/10_01_2026/UNION_-_-.jpeg>)
 ![RESULTADO UNION](<Imagenes Prototipo/10_01_2026/RESULTADO UNION.jpeg>)

 3. probamos que el panel solar funcione de manera correcta,nos dio un respectivo valor de 10.54V
 ![PRUEBA PANEL SOLAR](<Imagenes Prototipo/10_01_2026/PRUEBA PANEL SOLAR.jpeg>)

 4. conectamos el panel solar a los pines del protoboard
 ![CONEXION AL PANEL SOLAR](<Imagenes Prototipo/10_01_2026/CONEXION AL PANEL SOLAR.jpeg>)

 5. utilizamos un condensador de poliester de 1000nF, un pin se conecta al positivo del panel solar
 ![CONDENSADOR 1000nF](<Imagenes Prototipo/10_01_2026/CONDENSADOR 1000N.jpeg>)

 6. de la salida del condensador se conecta al pin 2 del chip LM358P
 ![CHIP PIN 2](<Imagenes Prototipo/10_01_2026/CHIP PIN 2.jpeg>)

 7. usamos una resistencia de gran valor en este caso 181K desde el respectivo pin 2 al pin output (Pin 1)
 ![RESITENCIA](<Imagenes Prototipo/10_01_2026/RESISTENCIA POTENCIA.jpeg>)

 8. del pin 3 del chip vamos poner un potenciometro de 10K, de la misma manera lo energizamos
 ![CABLEADO POTENCIOMETRO 1](<Imagenes Prototipo/10_01_2026/CABLEADO POTENCIOMETRO.jpeg>)
 ![POTENCIOMETRO SUP](<Imagenes Prototipo/10_01_2026/POTENCIOMETRO SUP.jpeg>)
 ![POTENCIOMETRO FRON](<Imagenes Prototipo/10_01_2026/POTENCIOMETRO FRON.jpeg>)
 
 9. del pin 1 del amplificador lo conectamos hasta el chip LM358P del comparador, especificamente al 3
 ![CONEXION SEGUNDO CHIP](<Imagenes Prototipo/10_01_2026/PIN 1- CHIP2.jpeg>)
 
 10. ubicamos un segundo amplificador, al pin 2, se energiza respectivamente
 ![CABLEADO SEGUNDO POTENCIOMETRO](<Imagenes Prototipo/10_01_2026/CABLEADO SEGUNDO POTENCIOMETRO.jpeg>)
 ![SEGUNDO POTENCIOMETRO](<Imagenes Prototipo/10_01_2026/2 POTENCIOMETRO FRONTAL.jpeg>)
 
 11. energizamos ambos chips
 ![ENERGIZAR CHIPS](<Imagenes Prototipo/10_01_2026/ENERGIZAMOS CHIP.jpeg>)
 
 12. damos una salida del segundo comparador
 ![OUTPUT SEGUNDO CHIP](<Imagenes Prototipo/10_01_2026/OUTPUT SEGUNDO CHIP.jpeg>)

 13. por la parte del DC, ponemos el inductor
 ![INDUCTOR](<Imagenes Prototipo/10_01_2026/INDUCTOR.jpeg>)

 14. ubicamos un condensador de 1000uF, para almacenar la energia, se aterriza
 ![CONDENSADOR 1000uF](<Imagenes Prototipo/10_01_2026/CONDENSADOR 1000uF.jpeg>)
 ![GND CONDENSADOR](<Imagenes Prototipo/10_01_2026/ATERRIZADA CONDENSADOR.jpeg>)

 15. conectamos el arduino nano, el cual va al pin 0, y al respectivo 5V y GND, lo conectamos a la banda de energia inferior del protoboard
 ![PINES ARDUINO](<Imagenes Prototipo/10_01_2026/PINES ARDUINO.jpeg>)

 16. ubicamos un led con su respectiva resistencia (220), en la salida DC
 ![LED_DC](<Imagenes Prototipo/10_01_2026/LED_DC.jpeg>)
 ![FUNCIONAMIENTO](<Imagenes Prototipo/10_01_2026/FUNCIONAMIENTO_LED.jpeg>)
 ### Resultado:
 se observa que el respectivo led se prende de manera correcta

 17. proyectamos el laser al panel solar
 ![LASER CRUZ](<Imagenes Prototipo/10_01_2026/LASER CRUZ.jpeg>)
 ### Observacion:
 se observa que el laser de cruz sale por fuera del respectivo panel, por lo cual no aprovecha todo el potencial del laser por lo consiguiente se opta por poner un laser de punto

 18. se conecta el Laser de punto
 ![LASER PUNTO](<Imagenes Prototipo/10_01_2026/LASER PUNTO.jpeg>)

 19. se programa el arduino para encender el laser 1 seg y apagarlo 1 seg
 [Codigo encender apagar](<Codigo Prototipo/10_01_2026/ENC_APA/ENC_APA.ino>)
 <video controls src="Videos Prototipo/10_01_2026/1 SEG-1SEG.mp4" title="PUNTO, OOK 1seg"></video>

 20. se observa el serial plotter del arduino 
 <video controls src="Videos Prototipo/10_01_2026/SERIAL PLOTTER.mp4" title="SERIAL PLOTTER"></video>
 ### Observacion
 se observa una señal con demasiado ruido aunque si funciona el Bias-t, no distingue la luz ambiente con el laser, tambien se observa que el panel solar es muy grande para realizar esta prueba ya que es de 11x9 cm aprox, esto hace que recolecte demasiado ruido, cuando se tapa el laser se observa que sigue recibiendo los mismos pulsos, ademas si cambia la señal cuando se ajusta con el potenciometro que lo que hacen uno es elevar el voltaje y el otro es el comparador que hace que funcione el trigger (disparador)

 21. se prueba el primer potenciometro para observar si si esta elevando el nivel de la señal, ya que este es el de referencia, como se observo en la simulacion
 <video controls src="Videos Prototipo/10_01_2026/POTENCIOMETRO 1.mp4" title="POTENCIOMETRO 1"></video>
 ### Resultado
 funciona de manera correcta, aun asi no se logro detecta o diferenciar la señal

---

## Fecha: 11/01/2026
**Fase:** Prototipado Real
**Bloque:** Panel solar, Bias TEE

## Objetivo:
Buscar y mejorar la sensisibilidad del circuito para lodrar diferenciar la señal ambiente a la señal del laser

## Metodologia:
 1. se observa que hubo una mala conexion desde el amplificador hasta el comparador ya que estaba conectado al pin 3, y la respectiva conexion es al pin 2 por lo cual, de pronto era una de los problemas que tenia el circuito
 2. de la misma forma, se quita el led del nodo DC y se agrega al output del comparador para comprender los altos y bajos que se presenta del comparador
 [CIRCUITO ARREGLADO](<Imagenes Prototipo/11_01_2026/CIRCUITO ARREGLADO.jpeg>)
 ![GRAFICA SEÑAL](<Imagenes Prototipo/11_01_2026/SEÑAL COMPORTAMIENTO.png>)

### Observaciones
se observa que la señal todavia tiene mucho ruido y no diferencia la señal que es emitida por el laser

---

## Fecha: 12/01/2026
**Fase:** Desarrollo prototipo 
**Bloque** Filtro RC Pasabajo, Panel solar

## Objetivo
mejorar el ruido que pueda presentar el sistema, que permita diferenciar el pulso del laser de la luz ambiente, del mismo modo hacer mas eficiente el sistema

## Metodologia
 1. como alternativa a reducir la capacitancia paracita del panel solar, se realizo un protector con carton dejando un espacio de 4x4cm, esto con el fin de reducir tanto el ruido como la capacitancia paracita
 ![MOLDE](<Imagenes Prototipo/12_01_2026/MOLDE.jpeg>)
 ![RECORTE 4X4 CM](<Imagenes Prototipo/12_01_2026/RECORTE 4X4 CM.jpeg>)
 ![4X4 CM](<Imagenes Prototipo/12_01_2026/4X4 cm.jpeg>)

 2. se conecta una resistencia de 1k junto al capacitor anterior de 1000nF, esto con el fin de realizar un Filtro RC Pasa-alto, permitiendo pasar asi frecuencias mayores a 159kHZ de la misma forma se cambio la resistencia de 181K, por 600K para mejorar la relacion de potencia
 ![RC PASA ALTO](<Imagenes Prototipo/12_01_2026/FILTRO PASA ALTO.jpeg>)
![CIRCUITO COMPLETO](<Imagenes Prototipo/12_01_2026/CIRCUITO COMPLETO.jpeg>)
 3. se implementa en el receptor un codigo de arduino que permita identificar, la frecuencia de 5khz gracia al inpulse, de la misma manera se visualiza por medio del LED
<video controls src="Videos Prototipo/12_01_2026/COMPLETO.mp4" title="CIRCUITO COMPLETO RECEPCION DE SEÑALES"></video>

[RECEPCION 5KHZ](<Codigo Prototipo/12_01_2026/Recibir_5khz/Recibir_5khz.ino>)

![SEÑAL PULSO PWM](<Imagenes Prototipo/12_01_2026/ANALISIS DE SEÑALES.png>)

### Observaciones
 se observa que en el codigo detecta los pulsos altos del sistema, sin embargo no reconoce todos los pulsos solo es posible de graduando manualmente los potenciometros, aunque al rato se encienda y se mantenga el alto, el problema es que aunque se tape el panel solar sigue detectando el mismo ruido y se sigue comportando de la misma forma, aunque con el filtro el sistema se estabilizo de la mejor manera
 
### Decision 
ya que el circuito es muy inestable presenta mucha capacitancia, y los potenciometros toca ajustarlos segun las circunstancias del ambiente, por lo cual se desea implementar un modulo que permite que esta comparacion sea mas eficaz y estable, ya que es una un PCB, que es un circuito ya soldado y calibrado, no presenta problemas como el protoboard que cualquier cable suelto puede generar interferencia, ademas tiene led que nos dice si el laser lleva la misma sintonia que el modulo, igualmente bajar la frecuencia ya que es muy rapida para su fotodeteccion

---

## Fecha: 12/01/2026
**Fase:** simulaciones
**Bloque** Simulador comparador LM393

## Objetivo
probar el comparador LM393 comprobando si permite diferenciar entre el Ruido ambiente y la señal emitida por el Haz de luz, de la misma manera identificar cual sistema es mas eficaz en este sentido

## Metodologia
1. Realizar una simulacion por medio de proteus probando el funcionamiento del Modulo LM393, que permita comprender la eficiencia de este comparador a la eficiencia del LM358P 
2. analizar la grafica de analisis del sistema PWM

## Resultado
[Simulacion LM393](<../Simulaciones/Comparador LM393/Docs/LM393.md>)

---

## Fecha: 15/01/2026
**Fase:** Desarrollo Prototipo
**Bloque:** Implementacion LM393

## Objetivo
Comprobar como se comporta el modulo LM393, taanto en su eficiencia como en su respectiva estabilidad logrando, asi identificar los pequeños cambios que presenta la modulacion PWM, por lo mismo se incorpora su uso en el actual proyecto, permitiendo analizar posibles problemas o fortalezas del sistema.

## Metodologia
1. se desolda el respectivo LDR, en donde se implentara el panel solar que actuaria como receptor de luz
![Modulo Completo LDR](<Imagenes Prototipo/15_01_2026/Modulo LDR.jpeg>)
![Desoldado](<Imagenes Prototipo/15_01_2026/Desoldado.jpeg>)

2. el panel solar le reducimos la zona de recepcion aun mas, con el fin de reducir el ruido generado por la luz
![Reducion Zona](<Imagenes Prototipo/15_01_2026/Reduccion Zona .jpeg>)
![Reduccion Zona](<Imagenes Prototipo/15_01_2026/Prueba Panel Solar.jpeg>)

3. se solda el panel solar al modulo LM393, por esto se implementan dos pines para la respectiva conexion con jumpers al protoboard para poder utilizar el filtro pasa altos
![alt text](<Imagenes Prototipo/15_01_2026/Pin Entrada.jpeg>)

4. se incorpora en el protoboard un filtro pasa altos, que permita tanto convertir la señal en AC, como en dejar pasar solo una frecuencia, en este caso usamos un condensador 1000nf y 10k de resistecia de 1k ohm, dandonos como resultado la deteccion de frecuencias mayores a 159Hz, evitando asi las frecuencias como las bombillas que en Latino America es de 60Hz
![Filtro Pasa Alto](<Imagenes Prototipo/15_01_2026/Filtro Pasa Alto.jpeg>)

5. Se procede a conectar el panel solar al protoboard, en el in del filtro
![Conexion panel solar](<Imagenes Prototipo/15_01_2026/Conexion panel Solar.jpeg>)

6. se conecta el out del filtro al modulo LM393, en donde se encuentra ya filtrada la luz
![Conexion Filtro - Panel solar](<Imagenes Prototipo/15_01_2026/Conexion al modulo LM393.jpeg>)

5. se procede a conectar el arduino al out del modulo LM393, permitiendo leer la salida del sistema, energizamos el modulo y del mismo modo utilizamos el pin digital (D2), para permitir observar los respectivos cambios del sistema
![Conexion arduino](<Imagenes Prototipo/15_01_2026/Conexion Modulo al Arduino.jpeg>)


![Cmprobamos el sistema completo](<Imagenes Prototipo/15_01_2026/Sistema completo.jpeg>)

### Resultados
el sistema se comporto de la misma forma que con el sistema anterior, detecta mucho ruido ambiente, por lo cual no permite diferenciar estos cambios en la transmision, aunque si se comporta mas estable, no se obtiene el resultado esperado, ya que se ajustaba el potenciometro del modulo, pero el cambio mas minimo hacia que no la luz led del modulo presentara valores no esperados, tambien es importante reiterar que si funcionara de esta forma se debe ajustar cada vez que se cambie de ambiente, ya que la recepcion de señal seria distinta, por otro lado las señales que se observaron en el serial Plotter, son iguales a las presentadas por el LM358p

### Decision
como alternativa, es cosiderable utilizar un filtro optico de color rogo, que permita filtrar las ondas de luz visible, permitiendo ingresar solo la longitud de onda de color rojo, esto con el fin de reducir drasticamente el ruido ambiente, permitir no reajustar cada vez que se cambia de escenario, del misma manera como conocemos que el panel no permitiria generar mucho voltaje se plantea realizar un array de paneles en donde unos permitan generar energia y otro recibir la informacion.

----

## Fecha: 30/01/2026
**Fase:** Desarrollo Prototipo
**Bloque:** Implementacion Filtro Optico

## Objetivo
comprobar el funcionamiento del sistema de comunicacion fso, utilizando un filtro optimo para optimizar la recepcion de datos por parte de los SATs, del mismo modo comprobar la velocidad, estabilidad y escalabilidad del sistema, probando modulaciones, filtros y sistemas de recepcion, asi como sistema de sincronizacion de datos y su respectiva seguridad

## Metodologia
1. conseguir un filtro optico color rojo
![Filtro Optico](<Imagenes Prototipo/30_01_2026/FILTRO ROJO.jpeg>)

2. colocar el filtro rojo sobre la superfidie del panel solar, con el fin de que al incidir la luz solo pase la luz roja
![Superponer FIltro al Panles](<Imagenes Prototipo/30_01_2026/FILTRO ROJO SOBRE PANEL.jpeg>)

3. recubir el vidrio con cinta permitiendo que no ingrese luz lateral, que pueda actuar como ruido en el sistema
![Recubrimiento Laterales](<Imagenes Prototipo/30_01_2026/SELLADO VIDRIO.jpeg>)

4. comprobar cuanto voltaje esta produciendo el panel solar, en tres distintos momentos
 con incidencia del laser + luz ambiente
 ![Incidencia Panel](<Imagenes Prototipo/30_01_2026/INCIDE LASER.jpeg>)

 sin incidencia del laser + luz ambiente
 ![Sin Incidencia](<Imagenes Prototipo/30_01_2026/PANEL SIN INCIDIR.jpeg>)

 panel 100% sin recepcion de luz
 ![Sin Luz alguna](<Imagenes Prototipo/30_01_2026/PANEL TAPADO.jpeg>)

5. a partir de esto se decide no hacer uso de ningun comparador, y probar el cambio generado por medio del ADC del arduino, funcionando asi como un Osciloscopio, observando los respectivos cambio entre un low y un high
<video controls src="Videos Prototipo/30_01_2026/Osciloscopio.mp4" title="Cambios Osciloscopio"></video>
<video controls src="Videos Prototipo/30_01_2026/SERIAL PLOTTER.mp4" title="Serial Plotter"></video>

[Codigo Osciloscopio](<Codigo Prototipo/30_01_2026/osciloscopio.ino>)

### Resultado
se observa que cuando no se incide el laser se encuentra en un nivel inferior o un valor ADC menor, pero cuando se incide aumenta tanto el nivel como la velocidad, ademas lo observado en el multimetro es el mismo fenomeno, concluyendo que el sistema logra diferenciar con gran diferencia el laser a la luz ambiente, con ento podemos empezar a digitalizar los datos segun su esto, pasando informacion analoga a Digital

6. se procede a probar modulacion On-Off keying, usando los siguientes codigos, el cual el sistema detecta y emite 1 segundo high y el segundo siguiente low
para el sistema de recepcion hacemos uso de un TH o umbral quiere decir que cuando el nivel ADC pasa un nivel, es un 1 y cuando es menor que ese th es 0, este th se calcula (ADCmx + ADCmn)/2-

niveles ADC
![Niveles ADC mayor](<Imagenes Prototipo/30_01_2026/ADC_MAYOR.png>)
![Niveles ADC menor](<Imagenes Prototipo/30_01_2026/ADC_MENOR.png>)

Codigo OOK
[Laser OOK](<Codigo Prototipo/30_01_2026/OOK/LASER_ON_OFF.ino>)
[Laser On](<Codigo Prototipo/30_01_2026/OOK/RECEPCION_ON_OFF.ino>)

### Resultado
![Resultado](<Imagenes Prototipo/30_01_2026/PRUEBA ON-OFF.png>)
como se observa que cuando el laser esta en high en el laser el sistema lo detecta de manera correcta imprimiendo ON, y cuando se encuentra apagado, detecta el OFF, tambien nos damos que tenemos buena diferencia entre la señal apagada y encendida

7. a partir de esto, podemos hacer deteccion de bits de informacion, el principio es transmitir una serie de on off en serie, y que llegue de manera efectiva en el receptor, pero en forma de 1 y 0. formando asi un byte

[Codigo Laser Bits](<Codigo Prototipo/30_01_2026/BITS/BITS_LASER.ino>)
[Codigo Receptor Bits](<Codigo Prototipo/30_01_2026/BITS/BITS_RECEPTOR.ino>)

<video controls src="Videos Prototipo/30_01_2026/BITS FSO.mp4" title="Bits"></video>

### Resultado 
se obtiene una optima recepcion de los bits
![Bits](<Imagenes Prototipo/30_01_2026/Prueba Bits.png>)

### Observaciones
en este sistema presenta dos principales problemas, una de ellas es la sincronizacion entre el emisor y receptor ya que el byte, no sabe donde inicia el mensaje y donde lo finaliza, ademas de eso se esta realizando con una comunicacion lenta, por lo cual casi no hay errores, sin embargo para la transmision de telemetria se debe mejorar considerablemente la velocidad de transmision

### Decision
para la velocidad se debe ajustar la velocidad de corte, se debe mejorar del mismo modo la manera en que se piensan transmitir los mensajes, ya que se debe ajustar por protocolo, igualmente, utilizar timer, reducir la frecuencia o aumentarla segun el caso,utilizar un sistema para la sincronizacion correcta de los datos, para lograr asi transmitir Telemetria de manera eficiente

---


## Fecha: 13/02/2026
**Fase:** Desarrollo Prototipo
**Bloque:** Desarrollo logaritmo (Estados)

## Objetivo
permitir que el panel solar detecte niveles de estado de alerta, por medio de pulsos opticos, permitiendo general distintos umbrales a partir del estado del fenomeno analizado.

## Metodologia
1. dejamos el mismo sistema usado en el desarrollo realizado en el punto anterior, pero se procede a probar un metodo diferete tanto de comunicacion como de recepcion, teniendo en cuentas las limitaciones fisicas del panel como fotodetector.

2. cargamos el codigo del emisor
[Codigo Laser](<Codigo Prototipo/13_02_2026/ESTADO_SAT_LASER/ESTADO_SAT_LASER.ino>)

### Resultados
primero declaramos los pines ya previamente definidos, igualmente inicialiazamos la variable de el estado del sitema (currentstate), guardamos el instante en milisegundos desde que el arduino arranco, siendo util para poder medir intervalos de 1 seg, a partir de esto creamos un for para decir que cada vez que se ingrese por serial un 1 haya un pulso de 200ms (100 on y 100 of), si se ingresa un 2, (3 pulsos de 200) y el 3, 6 pulsos correspondientemente, ademas se implementa un while para mantener el laser apagado 1 segundo (pulso + silencio), denominado (busy-wait), para finalizar configuramos la salida digital en el pin 9, y imprimimos la opcion de estado, permitimos el leer caracter desde el serial y realizamos su relacion con el estado para afectuar el pulso correspondiente

3. cargamos el codigo del receptor 
[Codigo Panel](<Codigo Prototipo/13_02_2026/ESTADO_SAT_PANEL/ESTADO_SAT_PANEL.ino>)

### Resultado
establecemos el pin del panel solar (A0), usamos el margen de deteccion quiere decir que solo considera pulsos superiores a un min, para reducir ruido, variables para inicio del segundo, para el numero de pulsos detectados en cada ventana, y numero de ventanas consecutivas sin pulsos, asi como el estado anterior de la señal, instante en el que inicio el pulso permitiendo detectar flancos, a partir de esto el arduino en este caso lee 10 veces y promedia (Reduccion del ruido) esto se le llama filtro promedio movil (Filto pasa bajos digital), suaviza la señal pero reduce la respuesta dinamica del sistema.

calibramos la base, se mide la liz ambiente durante 1.5 seg, se estima el nivel DC del canal optico, y se fija el nivel de referencia, para finalizar se convierte la señal analoga en digital (Binario), se valida la duracion de cada pulso (Debe durar 60ms) y cada seg se valida el estado del sistema, y se clasifica el estado, se reinicia la ventana y actualiza el estado

4. se procede hacer las pruebas del PCM, permitiendo validar que el panel solar los detecta de manera optima

 Estado en el que el sistema se encuentra estable
 <video controls src="Videos Prototipo/12_02_2026/Estado Estable.mp4" title="Estable"></video>

 Estado en el que el sistema se encuentra en alerta
 <video controls src="Videos Prototipo/12_02_2026/Estado Alerta.mp4" title="Alerta"></video>

 Estado en el que el sistema se encuentra en emergencia
 <video controls src="Videos Prototipo/12_02_2026/Estado emergencia.mp4" title="Emergencia"></video>

### Decision
se plantea completar el sistema emisor, para eso se planea diseñar una estructura electronica, capaz de auto direccionarse, o concentrar el laser en distintos puntos por medio de servomotores, del mismo modo dejar listo para el montaje en la "maqueta", asi como la adecuacion del sistema de energia, para permitir tener mas practicidad en la evolucion de pruebas

por otro lado, se desea probar paneles de menores tamaños para comprobar su comportamiento y su respectiva capacitancia, para ir probando de manera paralela el funcionamiento de sistemas en mayor velocidad y con uso de modulacion mas estables y mas robusta

----