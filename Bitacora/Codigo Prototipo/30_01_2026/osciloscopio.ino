// --- CÓDIGO OSCILOSCOPIO (LECTURA DIRECTA) ---
// Conecta Panel al Pin A0

void setup() {
  // Usamos velocidad alta para que la gráfica sea fluida
  Serial.begin(115200); 
}

void loop() {
  // Leemos el voltaje crudo (0 a 1023)
  int lectura = analogRead(A0);
  
  // (Opcional) Convertimos a Voltios real para que tú lo entiendas
  // 5.0 es el voltaje del Arduino, 1023 es la resolución máxima
  float voltaje = lectura * (5.0 / 1023.0);
  
  // Imprimimos el valor
  Serial.print("Voltaje:"); // Etiqueta para el plotter
  Serial.println(voltaje);
  
  // Un delay minúsculo para estabilidad
  delay(5); 
}