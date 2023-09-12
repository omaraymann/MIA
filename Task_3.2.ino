int ech_1=2;
int trig_1=3;
int trig_2=4;
int ech_2=5;
int ech_3=6;
int trig_3=7;
int ech_4=8;  
int trig_4=9;
void setup() 
{
   Serial.begin(9600);
}
void loop() 
{
  long sensor_1=sensor_calc(trig_1,ech_1);
  long sensor_2=sensor_calc(trig_2,ech_2); 
  long sensor_3=sensor_calc(trig_3,ech_3);
  long sensor_4=sensor_calc(trig_4,ech_4);
  Serial.print("sensor 1=");
  Serial.println(sensor_1);
  Serial.print("sensor 2=");
  Serial.println(sensor_2);
  Serial.print("sensor 3=");
  Serial.println(sensor_3);
  Serial.print("sensor 4=");
  Serial.println(sensor_4);
  Serial.println("x-axis");
  Serial.println(calculateXcoordinate(sensor_1,sensor_4));
  Serial.println("y-axis");
  Serial.println(calculateXcoordinate(sensor_2,sensor_3));
}
long microsecondsToCentimeters(long microseconds)
{
   return (microseconds / 29 / 2);
}
long sensor_calc(int trig , int echo)
{
   long duration, inches, cm;
   pinMode(trig, OUTPUT);
   digitalWrite(trig, LOW);
   delayMicroseconds(2);
   digitalWrite(trig, HIGH);
   delayMicroseconds(10);
   digitalWrite(trig, LOW);         
   pinMode(echo, INPUT);
   duration = pulseIn(echo, HIGH);
   cm = microsecondsToCentimeters(duration);
  return cm;
}
long calculateYcoordinate(long downDistance,long UpDistance)
{
  long y = (UpDistance - downDistance)/2;
  return constrain(y,0.0,600);
  
}
long calculateXcoordinate(long rightDistance,long leftDistance)
{
  long x = (rightDistance - leftDistance)/2;
  return constrain(x,0,500);
  
}