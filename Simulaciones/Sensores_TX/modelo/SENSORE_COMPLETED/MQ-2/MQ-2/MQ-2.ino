#include <LiquidCrystal.h>

LiquidCrystal lcd (12,11,5,4,3,2);
int sensorValue;
int buzzerPin;

void setup() 
{
  lcd.begin (20,2);
}

void loop() {
  sensorValue =analogRead (A0);
  float gasSensor = sensorValue*(5.0/1023.0); //conversion a voltaje
     lcd.setCursor (0,0);
     lcd.print ("Valor :    ");
     lcd.print (gasSensor);
  if (gasSensor >=0.7)
  {
    digitalWrite (buzzerPin, HIGH);
    lcd.setCursor (0,0);
    lcd.print (gasSensor);
    delay (100);
    lcd.setCursor (0,1);
    lcd.print ("Gas Detectado");
  }
  else if (gasSensor < 0.7)
  {
    digitalWrite (buzzerPin, LOW);
    lcd.setCursor (0,0);
    lcd.print ("Valor:     ");
    lcd.print (gasSensor);
    delay (100);
    lcd.setCursor (0,1);
    lcd.print ("No Hay Fuga   ");
  }
}