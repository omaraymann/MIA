#include <Wire.h>
#define bottom1 3
#define bottom2 2
//define a slave for I2C
#define SLAVE_ADDR 9
void setup()
{
  Wire.begin();
  
  Serial.begin(9600);
  //set pin mode
  pinMode(bottom1,INPUT);
  pinMode(bottom2,INPUT);
  //initialize I2C communication as master
  
}

void loop()
{
  //read push bottom values
  int b1=digitalRead(bottom1);
  int b2=digitalRead(bottom2);
  
  Wire.beginTransmission(SLAVE_ADDR);
  Wire.write(b1);
  Wire.write(b2);
  Wire.endTransmission();
}