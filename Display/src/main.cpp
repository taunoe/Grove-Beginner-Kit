#include <Arduino.h>
#include <U8x8lib.h>
#include <Wire.h>
#include "DHT.h"  // Seed
#include "Seeed_BMP280.h"
#include "LIS3DHTR.h"  // 3-Axis Digital Accelerometer ±2g to 16g

/* Accelerometer LIS3DHTR */
LIS3DHTR<TwoWire> Accelerometer;//IIC
#define WIRE Wire


/* DHT11 */
#define DHTPIN 3
DHT dht(DHTPIN, DHT11);

/* BMP280 */
#define BMP280_DEBUG_PRINT
BMP280 bmp280;

/* Display */
U8X8_SSD1306_128X64_ALT0_HW_I2C display(/* reset=*/ U8X8_PIN_NONE);

void setup() {
  Serial.begin(115200);

  /* DHT11 */
  dht.begin();

  /* BMP280 */
  if (!bmp280.init()) {
    Serial.println("BMP280 not connected or broken!");
  }

  /* Accelerometer LIS3DHTR */
  Accelerometer.begin(WIRE, 0x19);
  delay(100);
  Accelerometer.setOutputDataRate(LIS3DHTR_DATARATE_50HZ);
  if (!Accelerometer) {
    Serial.println("LIS3DHTR didn't connect.");
    while (1);
    return;
  }

  /* Display */
  display.begin();
  display.setPowerSave(0); // 1-off
  display.setFlipMode(1);  // 0  or 1
}

void loop() {
  /* DHT11 */
  float temp, humi;
  temp = dht.readTemperature();
  humi = dht.readHumidity();

  float pressure, bmp_temp, altitude;

  /* BMP280 */
  pressure = bmp280.getPressure();
  bmp_temp = bmp280.getTemperature();
  altitude = bmp280.calcAltitude(pressure);

  Serial.print("Temp: ");
  Serial.print(bmp_temp);
  Serial.println("C");
  Serial.print("Pressure: ");
  Serial.print(pressure);
  Serial.println("Pa");
  Serial.print("Altitude: ");
  Serial.print(altitude);
  Serial.println("m");


  /* Accelerometer LIS3DHTR */
  float x, y, z;
  x = Accelerometer.getAccelerationX();
  y = Accelerometer.getAccelerationY();
  z = Accelerometer.getAccelerationY();

  Serial.print("x:");
  Serial.print(x);
  Serial.print("\t");
  Serial.print("y:");
  Serial.print(y);
  Serial.print("\t");
  Serial.print("z:");
  Serial.println(z);
  

  /* Display */
  display.setFont(u8x8_font_chroma48medium8_r);
  
  display.setCursor(0, 0);  // y, y
  display.print("Hello World!");

  display.setCursor(0, 33);
  display.print("Temp:");
  display.print(temp);
  display.print("C");

  display.setCursor(0,50);
  display.print("Humidity:");
  display.print(humi);
  display.print("%");

  display.refreshDisplay();

  delay(200);
}