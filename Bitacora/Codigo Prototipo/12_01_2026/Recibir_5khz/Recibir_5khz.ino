void setup() {
  // Velocidad alta para no perdernos detalles rápidos
  Serial.begin(115200); 
  
  // Tu entrada desde el comparador
  pinMode(7, INPUT);
}

void loop() {
  // Leemos el estado del comparador (0 o 1)
  int estado = digitalRead(7);
  
  // OPCIONAL: Si quieres ver "ruido" analógico,
  // conecta también el Pin 3 del chip al A0 del Arduino y descomenta abajo:
  // int analogico = analogRead(A0);
  
  // Imprimimos para el Plotter
  Serial.print("Comparador:");
  Serial.print(estado); // Esto dibujará una línea cuadrada (0 a 1)
  
  // Si descomentaste lo analógico:
  // Serial.print(" Señal:");
  // Serial.println(analogico);
  
  Serial.println(); // Salto de línea para el siguiente punto
  
  delay(2); // Pequeña pausa para estabilizar la gráfica
}