#include <avr/io.h>

char inByte;

void setup() {
  
  DDRD |= B00011100;
  PORTD = B00000000;
  
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:


  if(Serial.available() > 0){
    inByte = Serial.read();

    //First 3 bits of inByte controlls D2, D3 and D4
    PORTD = inByte<<2 & B00011100;
    if(inByte == B00011100){
      Serial.println("ok");
    }
  }
}
