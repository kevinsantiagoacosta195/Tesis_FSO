void setup() {
  pinMode(9, OUTPUT);

  // ---- TIMER1: PWM a 5 kHz ----
  TCCR1A = 0;
  TCCR1B = 0;

  // Fast PWM, TOP = ICR1
  TCCR1A |= (1 << COM1A1);   // PWM en pin 9
  TCCR1A |= (1 << WGM11);
  TCCR1B |= (1 << WGM12) | (1 << WGM13);

  // Prescaler = 8
  TCCR1B |= (1 << CS11);

  ICR1 = 399;     // TOP → 5 kHz
  OCR1A = 300;    // ~50% duty
}

void loop() {
  // nada aquí
}
