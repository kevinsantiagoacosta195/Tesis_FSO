const int laserPin = 9;
int currentState = 0;

void sendPulses(int n) {
  unsigned long start = millis();

  for (int i = 0; i < n; i++) {
    digitalWrite(laserPin, HIGH);
    delay(100);
    digitalWrite(laserPin, LOW);
    delay(100);
  }

  while (millis() - start < 1000) {
    digitalWrite(laserPin, LOW);
  }
}

void setup() {
  pinMode(laserPin, OUTPUT);
  Serial.begin(115200);
  Serial.println("0=ESTABLE 1=ALERTA 2=EMERGENCIA");
}

void loop() {

  if (Serial.available()) {
    char c = Serial.read();
    if (c == '0') currentState = 0;
    if (c == '1') currentState = 1;
    if (c == '2') currentState = 2;
  }

  if (currentState == 0) sendPulses(1);
  if (currentState == 1) sendPulses(3);
  if (currentState == 2) sendPulses(6);
}

