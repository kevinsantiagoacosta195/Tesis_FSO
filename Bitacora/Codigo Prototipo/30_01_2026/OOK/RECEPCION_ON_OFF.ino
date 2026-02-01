const int sensorPin = A0;
const int TH = 14;   // umbral entre 6 y 22

void setup() {
  Serial.begin(115200);
}

void loop() {
  int v = analogRead(sensorPin);

  if (v > TH) {
    Serial.println("LASER ON");
  } else {
    Serial.println("LASER OFF");
  }

  delay(500); // 50 Hz
}
