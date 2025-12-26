/*
  Prueba PWM + Transistor + LED + Shunt
  Pin PWM: D9
  MCU: Arduino UNO
*/



// Valores de duty para pruebas
//int dutyValues[] = {0, 64, 128, 192, 255};
// 0% , 25%, 50%, 75%, 100%

void setup() {
  pinMode(9, OUTPUT);
}

void loop()
 {
analogWrite(9,255);
}
