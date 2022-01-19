#include <Arduino.h>

const int buzzer_pin = 5;
const int pot_pin = A0;

int pot_value = 0;
int buz_value = 0;
int cont_value = 0;

void setup() {
  Serial.begin(115200);
  pinMode(buzzer_pin, OUTPUT);
}

void loop() {
  pot_value = analogRead(pot_pin);  // 0-1023

  cont_value = constrain(pot_value, 10, 240);
  // constrain(x, a, b)
  // Constrains a number to be within a range.
  // x: the number to constrain Allowed data types: all data types.
  // a: the lower end of the range. Allowed data types: all data types.
  // b: the upper end of the range. Allowed data types: all data types.

  Serial.print("pot_value: ");
  Serial.print(pot_value);
  Serial.print("\t");

  buz_value = map(pot_value, 0, 1023, 0, 255);  // map(value, fromLow, fromHigh, toLow, toHigh)
  analogWrite(buzzer_pin, buz_value);  // 0-255

  Serial.print("buz_value: ");
  Serial.print(buz_value);
  Serial.print("\t");

  Serial.print("cont_value: ");
  Serial.print(cont_value);
  Serial.print("\n");

  delay(100);
}
