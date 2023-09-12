#include <Wire.h>
#define SLAVE_ADDR 9

void setup()
{
  //initialize pin mode
  pinMode(3,OUTPUT);
  
  //initialize I2C communication as slave
  Wire.begin(SLAVE_ADDR);
  
  //Function to run when data is received from master
  Wire.onReceive(receiveEvent);
  
  //setup serial monitor
  Serial.begin(9600);
 
}
void loop()
{
  delay(100);
}
void receiveEvent(int parameter)
{
  int b1=Wire.read();
  int b2=Wire.read();
  
  if(b1==0 && b2==0)
  {
    Serial.println("No message");
    analogWrite(3,0);
  }
  else if(b1==1 && b2==0)
  {
    Serial.println("Vector focused");
    analogWrite(3,128);
  }
  else if(b1==0 && b2==1)
  {
    Serial.println("Vector distracted");
    analogWrite(3,192);
  }
  else if(b1==1 && b2==1)
  {
    Serial.println("Glitch");
    analogWrite(3,255);
  }
}