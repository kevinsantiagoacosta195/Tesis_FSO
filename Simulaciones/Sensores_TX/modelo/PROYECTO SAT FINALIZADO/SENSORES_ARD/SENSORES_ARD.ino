#include <LiquidCrystal.h>
#include <Adafruit_BME280.h>
#include <SPI.h>

// -------- LCD --------
LiquidCrystal lcd(2, 3, A1, A2, A3, A4);

// -------- BME280 (SPI) --------
#define BME_CS 10
Adafruit_BME280 bme(BME_CS);

// -------- Pines --------
#define LED_TEMP 6
#define LED_HUM  8
#define LED_PRES 7
#define LED_DIST 9

#define TRIG_PIN 4
#define ECHO_PIN 5

#define GAS_PIN A0

// -------- Umbrales --------
float LIM_TEMP = 30.0;     // °C
float LIM_HUM  = 60.0;     // %
float LIM_PRES = 1000.0;   // hPa
float LIM_GAS  = 1.20;      // Voltios
int   LIM_DIST = 15;       // cm

void setup() {
  lcd.begin(16,2);

  pinMode(LED_TEMP, OUTPUT);
  pinMode(LED_HUM, OUTPUT);
  pinMode(LED_PRES, OUTPUT);
  pinMode(LED_DIST, OUTPUT);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  if (!bme.begin()) {
    lcd.print("BME280 ERROR");
    while (1);
  }
}

void loop() {

  // -------- BME280 --------
  int temp = bme.readTemperature();
  float hum  = bme.readHumidity();
  float pres = bme.readPressure() / 100.0;

  digitalWrite(LED_TEMP, temp > LIM_TEMP);
  digitalWrite(LED_HUM,  hum  > LIM_HUM);
  digitalWrite(LED_PRES, pres < LIM_PRES);

  // -------- Gas MQ-2 --------
  int gasRaw = analogRead(GAS_PIN);
  float gasV = gasRaw * (5.0 / 1023.0);

  // -------- HC-SR04 --------
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duracion = pulseIn(ECHO_PIN, HIGH);
  int distancia = duracion * 0.034 / 2;

  digitalWrite(LED_DIST, distancia < LIM_DIST);

  // -------- LCD --------
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("T:");
  lcd.print(temp,1);
  lcd.print(" H:");
  lcd.print(hum,0);
  lcd.print(" P:");
  lcd.print(pres,2);

  lcd.setCursor(0,1);
  lcd.print ("Distancia: ");
  lcd.print(distancia);
  lcd.print("cm     ");
  if (gasV > LIM_GAS)
  {
    lcd.print("Gas Detectado: ");
    lcd.print(gasV,1);
  }
  else
    lcd.print("No Hay Gas ");
    lcd.print(gasV,1);


  delay(1000);
}
