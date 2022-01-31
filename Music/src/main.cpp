#include <Arduino.h>
#include "pitches.h"

#define NTD0 -1
#define NTD1 294
#define NTD2 330
#define NTD3 350
#define NTD4 393
#define NTD5 441
#define NTD6 495
#define NTD7 556

#define NTDL1 147
#define NTDL2 165
#define NTDL3 175
#define NTDL4 196
#define NTDL5 221
#define NTDL6 248
#define NTDL7 278

#define NTDH1 589
#define NTDH2 661
#define NTDH3 700
#define NTDH4 786
#define NTDH5 882
#define NTDH6 990
#define NTDH7 112

#define DOUBLE 2
#define WHOLE 1
#define HALF 0.5
#define QUARTER 0.25
#define EIGHTH 0.25
#define SIXTEENTH 0.625

int tune[] = {
    NTD3, NTD3, NTD4, NTD5,
    NTD5, NTD4, NTD3, NTD2,
    NTD1, NTD1, NTD2, NTD3,
    NTD3, NTD2, NTD2,
    NTD3, NTD3, NTD4, NTD5,
    NTD5, NTD4, NTD3, NTD2,
    NTD1, NTD1, NTD2, NTD3,
    NTD2, NTD1, NTD1,
    NTD2, NTD2, NTD3, NTD1,
    NTD2, NTD3, NTD4, NTD3, NTD1,
    NTD2, NTD3, NTD4, NTD3, NTD2,

    NTD1, NTD2, NTDL5, NTD0,
    NTD3, NTD3, NTD4, NTD5,
    NTD5, NTD4, NTD3, NTD4, NTD2,
    NTD1, NTD1, NTD2, NTD3,
    NTD2, NTD1, NTD1};

float durt[] = {
    1, 1, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 1,
    1 + 0.5, 0.5, 1 + 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 1 + 0.5,
    0.5, 1 + 1, 1, 1,
    1, 1, 1, 0.5,
    0.5, 1, 1, 1,
    0.5, 0.5, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 0.5,
    0.5, 1, 1, 1,
    1, 1 + 0.5, 0.5, 1 + 1,
};

int length;
int tonepin = 5;
int ledpin = 4;

void setup()
{
  Serial.begin(115200);
  pinMode(tonepin, OUTPUT);
  pinMode(ledpin, OUTPUT);
  length = sizeof(tune) / sizeof(tune[0]);
}

void loop()
{
  /*
  for (int x = 0; x < length; x++)
  {
    tone(tonepin, tune[x]);
    digitalWrite(ledpin, HIGH);
    delay(400 * durt[x]);

    digitalWrite(ledpin, LOW);

    delay(100 * durt[x]);
    noTone(tonepin);
  }
  */
  for (int x = 0; x < length; x++)
  {
    tone(tonepin, tune[x]);
    Serial.println(tune[x]);
    delay(400 * durt[x]);
    delay(100 * durt[x]);
    noTone(tonepin);
  }
  delay(4000);
}
