const int sensorPin = A0;
const int TH = 14;
const int bitTime = 200;

int readBit() {
  int ones = 0;
  const int N = 5;

  for (int i = 0; i < N; i++) {
    if (analogRead(sensorPin) > TH) ones++;
    delay(bitTime / N);
  }
  return (ones > N/2);
}

bool detectStart() {
  while (analogRead(sensorPin) > TH);  // esperar idle

  unsigned long t0 = millis();
  while (analogRead(sensorPin) < TH) {
    if (millis() - t0 > 3 * bitTime) return true;
  }
  return false;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (detectStart()) {

    delay(2*bitTime + bitTime/4); // centro del primer bit

    for (int i = 0; i < 8; i++) {
      Serial.print(readBit());
    }
    Serial.println();

    delay(300);
  }
}

