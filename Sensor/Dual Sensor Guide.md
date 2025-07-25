# Dual Sensor Guide

## 1. Introduction
For a general start up guide on sensors, refer to [this guide from last year!](Dashboard/GUIDE.md)

## 2. Sensor Setup
In order to utilize 2 accelerometers, the sensors need to have different addresses for the Arduino to recognize that data is coming from different sources. The address pin is found on the back of the sensor. By soldering over the address pin (left) on one of the accelerometers, this will change its address from 0x68 to 0x69. 
      
<img width="430" height="286" alt="image" src="https://github.com/user-attachments/assets/a860107e-96ee-4cc1-a083-f7665f7b1958" /> <img width="439" height="285" alt="image" src="https://github.com/user-attachments/assets/fbdd0136-2462-4016-ab91-4721d036ccd2" />

Unfortunately, the DFRobot BMX160 Library in Arduino does not have a designated function to allow for the definition of 2 different addresses, as the address 0x68 is hard-coded in. To change this, we’ll have to modify the library itself.
1.	Navigate to the Arduino library. This will likely be in "C:\Users\Username\Documents\Arduino\libraries\DFRobot_BMX160"
2.	Open “DFRobot_BMX160.cpp” and “DFRobot_BMX160.h” in a code editor. If you don't have a code editor already installed, you can [download VSCode here!](https://code.visualstudio.com/download)
3.	In the .cpp file, find the begin() function and make the following changes below. Make sure to save! 

Original:
```c++
bool DFRobot_BMX160::begin()
{
    _pWire->begin();
    if (scan() == true){
        ...
    }
    else
        return false;
}
```
Modified:
```c++
bool DFRobot_BMX160::begin( uint8_t addr)
{
    _pWire->begin();
    _addr = addr; 
    if (scan() == true){
       ...
    }
    else
        return false;
}
```
4.	In the .h file, find the corresponding begin() function definition and the variable _addr. These should be at lines 988 and 1106 respectively. Make the following changes highlighted below.
Original: 
`    bool begin();`
Modified:
`    bool begin( ==uint8_t addr==);`
Original: 
`    uint8_t _addr == = 0x68==;`
Modified: 
`    uint8_t _addr;`

Now that the library has been modified, the begin function will set an address for each sensor and allow for differentiation between the data coming from the sensors. When you set up the sensors in Arduino, ensure that you specify the address of the sensor in your code as so:
```C
  if (!sensor1.begin(0x68)) { 
    Serial.println("Sensor 1 failed!");
    while (1);
  }
  if (!sensor2.begin(0x69)) {
    Serial.println("Sensor 2 failed!");
    while (1);
  }
```

## 3. Using Dual Sensors for Exercise Tracking
One effective application for these sensors is measuring the angle between two segments at a joint, allowing them to be used as a device for tracking range of motion. 

In summary, the code determines the angle between the "downward" direction of each sensor's measurement (based on their accelerometer readings) and uses that angle to approximate the joint angle. Both sensors measure acceleration in three dimensions (x, y, and z).

### 3.1. Code Breakdown
#### 1. Library and objects
```C
#include <DFRobot_BMX160.h>
DFRobot_BMX160 bmx160_bicep;
DFRobot_BMX160 bmx160_forearm;
```
- Include the sensor library and create two sensor objects

#### 2. Setup
```C
void setup() {
  Serial.begin(115200);

  // Initialize bicep (I2C 0x68, default)
  if (bmx160_bicep.begin(0x68) != true) { ... }
  
  // Initialize forearm (I2C 0x69, unique address)
  if (bmx160_forearm.begin(0x69) != true) { ... }
}
```
- Set up serial for debugging/printing
- Initialize both sensors at different addresses
- Halt if a sensor isn't found

#### 3. Read sensor data
```C
sBmx160SensorData_t Omagn_b, Ogyro_b, Oaccel_b;
sBmx160SensorData_t Omagn_f, Ogyro_f, Oaccel_f;

bmx160_bicep.getAllData(&Omagn_b, &Ogyro_b, &Oaccel_b);
bmx160_forearm.getAllData(&Omagn_f, &Ogyro_f, &Oaccel_f);
```
- Get data (acceleration, gyroscope, magnetometer) from each sensor
- This code uses acceleration only

#### 4. Calculate angle between acceleration vectors
```C
float dot = Oaccel_b.x * Oaccel_f.x + Oaccel_b.y * Oaccel_f.y + Oaccel_b.z * Oaccel_f.z;
float mag_b = sqrt(Oaccel_b.x * Oaccel_b.x + Oaccel_b.y * Oaccel_b.y + Oaccel_b.z * Oaccel_b.z);
float mag_f = sqrt(Oaccel_f.x * Oaccel_f.x + Oaccel_f.y * Oaccel_f.y + Oaccel_f.z * Oaccel_f.z);
```
- Dot product and magnitude (length) of each acceleration vector
```C
float angle_deg = 0;
if (mag_b > 0 && mag_f > 0) {
  float angle_rad = acos(dot / (mag_b * mag_f));
  angle_deg = angle_rad * 180.0 / PI;
}
```
- Angle between the two vectors, in radians, then converted to degrees

#### 5. Output data
```C
Serial.print("Elbow Angle: ");
Serial.print(angle_deg);
Serial.println(" degrees\n");
```
- Print the measured angle

### 3.2. How this works
At rest, the largest static acceleration is from gravity (downward) and all sensors measure this. By comparing the directionality (vector) of gravity detected by each sensor:

- If your arm is straight, both bicep and forearm “sense” gravity in the same direction — angle ≈ 0°
- If you bend your elbow to 90°, the forearm sensor will measure gravity at ~90° relative to the bicep — angle ≈ 90°
- If you bend it fully, ~180°, the sensors will be anti-parallel.

The calculation is purley geometric: the angle between the sensors' gravity vectors

### 3.3. Limitations
- It assumes sensors move as rigid segments with the limb
- Assumes only gravity or slow/static movement; rapid movement or other accelerations can disturb readings
