const int LASER_PIN = 9;
const int bitTime = 200;

void sendBit(int b) {
  digitalWrite(LASER_PIN, b ? HIGH : LOW);
  delay(bitTime);
}

void sendByte(byte data) {
  // START fuerte
  digitalWrite(LASER_PIN, LOW);
  delay(3 * bitTime);

  // bits MSB primero
  for (int i = 7; i >= 0; i--) {
    sendBit((data >> i) & 1);
  }

  // stop
  digitalWrite(LASER_PIN, LOW);
  delay(bitTime);
}

void setup() {
  pinMode(LASER_PIN, OUTPUT);
}

void loop() {
  sendByte(0b00010110);  // patrón de prueba
  delay(500);
}
