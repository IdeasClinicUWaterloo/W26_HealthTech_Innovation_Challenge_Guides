#include <DFRobot_BMX160.h>

DFRobot_BMX160 sensor1;
DFRobot_BMX160 sensor2;
const int touch_pin = 8;

void setup() {
  Serial.begin(115200);
  pinMode(touch_pin, INPUT); 
 
  if (!sensor1.begin(0x68)) { //make sure to include the corresponding address of the sensor
    Serial.println("Sensor 1 failed!");
    while (1);
  }
  if (!sensor2.begin(0x69)) {
    Serial.println("Sensor 2 failed!");
    while (1);
  }
}

void loop() {
  int pressed = digitalRead(touch_pin);
  //the getAllData function requires a magnometer variable but we're not actually using it 
  sBmx160SensorData_t acc1, gyro1, mag1;
  sBmx160SensorData_t acc2, gyro2, mag2;

  sensor1.getAllData(&mag1, &gyro1, &acc1);
  sensor2.getAllData(&mag2, &gyro2, &acc2);

  // if pressed, will send 1, otherwise 0
  Serial.print(pressed); Serial.print(','); 
  //send the accelerometer readings from first sensor
  Serial.print(acc1.x); Serial.print(',');
  Serial.print(acc1.y); Serial.print(',');
  Serial.print(acc1.z);Serial.print(',');
  //send the gyroscope readings from the first sensor
  Serial.print(gyro1.x); Serial.print(',');
  Serial.print(gyro1.y); Serial.print(',');
  Serial.print(gyro1.z);Serial.print(',');
  //send the accelerometer readings from second sensor
  Serial.print(acc2.x); Serial.print(',');
  Serial.print(acc2.y); Serial.print(',');
  Serial.print(acc2.z);Serial.print(',');
  //send the gyroscope readings from the second sensor
  Serial.print(gyro2.x); Serial.print(',');
  Serial.print(gyro2.y); Serial.print(',');
  Serial.print(gyro2.z);
  
  Serial.println("");

  delay(20);

}
