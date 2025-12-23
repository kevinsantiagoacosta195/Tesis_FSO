#include <SPI.h>
#include <Adafruit_BME280.h>

// --------------------
// Definición de pines
// --------------------
#define BME_CS 10

#define LED_TEMP 6
#define LED_HUM  7
#define LED_PRES 8

// --------------------
// Objeto BME280 (SPI)
// --------------------
Adafruit_BME280 bme(BME_CS);

// --------------------
// Umbrales
// --------------------
const float TEMP_UMBRAL = 30.0;   // °C
const float HUM_UMBRAL  = 60.0;   // %
const float PRES_UMBRAL = 1000.0; // hPa

void setup() {
  Serial.begin(9600);
  delay(1000);

  pinMode(LED_TEMP, OUTPUT);
  pinMode(LED_HUM, OUTPUT);
  pinMode(LED_PRES, OUTPUT);

  digitalWrite(LED_TEMP, LOW);
  digitalWrite(LED_HUM, LOW);
  digitalWrite(LED_PRES, LOW);

  if (!bme.begin()) {
    Serial.println("ERROR: BME280 no detectado");
    while (1);
  }

  Serial.println("BME280 inicializado correctamente");
}

void loop() {
  float temperatura = bme.readTemperature();        // °C
  float humedad     = bme.readHumidity();           // %
  float presion     = bme.readPressure() / 100.0;   // hPa

  // -------- Mostrar datos --------
  Serial.print("Temp: ");
  Serial.print(temperatura);
  Serial.print(" °C | Hum: ");
  Serial.print(humedad);
  Serial.print(" % | Pres: ");
  Serial.print(presion);
  Serial.println(" hPa");

  // -------- Alertas --------
  digitalWrite(LED_TEMP, temperatura > TEMP_UMBRAL);
  digitalWrite(LED_HUM,  humedad > HUM_UMBRAL);
  digitalWrite(LED_PRES, presion < PRES_UMBRAL);

  delay(1000);
}
