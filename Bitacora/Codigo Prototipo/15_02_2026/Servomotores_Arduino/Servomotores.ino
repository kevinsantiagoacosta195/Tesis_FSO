#include <Servo.h>

Servo servoX;
Servo servoY;

const int laserPin = 9;   // Láser en pin 9
bool laserState = false; // Estado del láser

int posX = 90;
int posY = 90;

void setup() {
  servoX.attach(10);
  servoY.attach(11);

  pinMode(laserPin, OUTPUT);
  digitalWrite(laserPin, LOW); // láser apagado al inicio

  servoX.write(posX);
  servoY.write(posY);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();

    // Movimiento
    if (c == 'w') posY += 2;
    if (c == 's') posY -= 2;
    if (c == 'd') posX -= 2;
    if (c == 'a') posX += 2;

    // Centrar
    if (c == 'r') {
      posX = 90;
      posY = 90;
    }

    // Láser ON / OFF
    if (c == 'l') {
      laserState = !laserState;
      digitalWrite(laserPin, laserState ? HIGH : LOW);
    }

    posX = constrain(posX, 0, 180);
    posY = constrain(posY, 0, 180);

    servoX.write(posX);
    servoY.write(posY);
  }
}