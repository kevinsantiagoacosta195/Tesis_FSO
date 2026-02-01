// EMISOR – Arduino Nano
const int LASER_PIN = 9;

void setup() {
  pinMode(LASER_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LASER_PIN, HIGH);  // ON
  delay(500);

  digitalWrite(LASER_PIN, LOW);   // OFF
  delay(500);
}

