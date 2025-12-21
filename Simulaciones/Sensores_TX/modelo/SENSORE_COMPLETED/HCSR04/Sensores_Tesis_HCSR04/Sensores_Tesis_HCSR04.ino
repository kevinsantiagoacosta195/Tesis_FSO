// Definición de pines para el sensor y la alarma
const int TRIG = 3;
const int ECHO = 2;
const int LED_ALARMA = 7; // El LED indica riesgo de desbordamiento

// Configuración de umbral (en centímetros)
const int UMBRAL_CRITICO = 10; 

long duracion;
int distancia;

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(LED_ALARMA, OUTPUT);
  
  Serial.begin(9600); // Monitoreo en tiempo real
}

void loop() {
  // Disparo del sensor ultrasónico
  digitalWrite(TRIG, LOW);
  delayMicroseconds(10);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  
  // Medición del tiempo de respuesta
  duracion = pulseIn(ECHO, HIGH);
  distancia = duracion * 0.034 / 2;

  // Lógica de alerta de desbordamiento
  // Si la distancia es menor al umbral, el nivel de agua es muy alto
  if (distancia > 0 && distancia <= UMBRAL_CRITICO) {
    digitalWrite(LED_ALARMA, HIGH); // Activar alerta
    Serial.print("¡ALERTA DE DESBORDAMIENTO! ");
  } else {
    digitalWrite(LED_ALARMA, LOW);  // Estado seguro
  }

  // Visualización de datos
  Serial.print("Nivel de proximidad (distancia al sensor): ");
  Serial.print(distancia);
  Serial.println(" cm");
  
  delay(500); // Lectura cada medio segundo
}