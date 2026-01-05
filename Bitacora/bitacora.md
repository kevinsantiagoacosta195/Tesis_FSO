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

3. 

[Simulacion Bias_t](../Simulaciones/Bias_T_Filtros/docs/BiaS_T.md)

## Observaciones 
se observa que el panel solar no permite transmision de alta velocidad, sin embargo apropiada para comunicacion de SATs.