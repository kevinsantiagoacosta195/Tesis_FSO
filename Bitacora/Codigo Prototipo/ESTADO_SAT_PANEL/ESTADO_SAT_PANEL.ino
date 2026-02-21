const int sensorPin = A0;

int baseLevel = 0;
int margin = 50;

unsigned long windowStart = 0;
int pulseCount = 0;
int noSignalCounter = 0;

bool lastLevel = false;
unsigned long pulseStart = 0;

int readAverage() {
  long sum = 0;
  for (int i = 0; i < 10; i++) {
    sum += analogRead(sensorPin);
    delayMicroseconds(200);
  }
  return sum / 10;
}

void calibrateBase() {
  long sum = 0;
  for (int i = 0; i < 300; i++) {
    sum += analogRead(sensorPin);
    delay(5);
  }
  baseLevel = sum / 300;
}

void setup() {
  Serial.begin(115200);
  delay(3000);
  calibrateBase();
  windowStart = millis();
  Serial.println("Receptor listo (modo robusto)");
}

void loop() {

  unsigned long now = millis();
  int value = readAverage();
  bool levelHigh = (value > baseLevel + margin);

  if (levelHigh && !lastLevel) {
    pulseStart = now;
  }

  if (!levelHigh && lastLevel) {
    if (now - pulseStart > 60) {
      pulseCount++;
    }
  }

  if (now - windowStart >= 1000) {

    if (pulseCount == 0) {
      noSignalCounter++;
    } else {
      noSignalCounter = 0;
    }

    if (noSignalCounter >= 3) {
      Serial.println("SIN ENLACE");
    }
    else {
      if (pulseCount == 1)
        Serial.println("ESTABLE");
      else if (pulseCount <= 4)
        Serial.println("ALERTA");
      else
        Serial.println("EMERGENCIA");
    }

    pulseCount = 0;
    windowStart = now;
  }

  lastLevel = levelHigh;
}
