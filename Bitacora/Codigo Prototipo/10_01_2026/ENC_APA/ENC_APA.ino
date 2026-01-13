void setup() {
  pinMode(9, OUTPUT); // Láser en el pin 9
}

void loop() {
  // --- PRENDIDO ---
  // Usamos tone 500Hz para que pase por tu condensador
  // Tu ojo lo verá como "PRENDIDO FIJO"
  tone(9, 500); 
  delay(1000); // Espera 1 segundo

  // --- APAGADO ---
  noTone(9);
  delay(1000); // Espera 1 segundo
}
