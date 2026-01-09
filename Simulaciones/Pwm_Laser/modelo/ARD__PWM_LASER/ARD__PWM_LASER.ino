void setup() {
  pinMode(9, OUTPUT);

  // Configuración para 5kHz exactos
  TCCR1A = 0; TCCR1B = 0; TCNT1 = 0;
  
  // Fast PWM, TOP en ICR1
  TCCR1A |= (1 << COM1A1) | (1 << WGM11);
  TCCR1B |= (1 << WGM12) | (1 << WGM13);
  TCCR1B |= (1 << CS11); // Prescaler 8

  ICR1 = 399;  // Frecuencia 5kHz
  OCR1A = 200; // Duty Cycle 50%
}

void loop() {
  // El láser ahora está transmitiendo una onda portadora de 5kHz
}