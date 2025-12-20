# Dual Accelerometers for Exercise Tracking
For the set up, refer to [Dual Accelerometer Guide](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Sensors/Dual_Accelerometer_Guide.md).

One effective application for these sensors is measuring the angle between two segments at a joint, allowing them to be used as a device for tracking range of motion. 

In summary, the code determines the angle between the "downward" direction of each sensor's measurement (based on their accelerometer readings) and uses that angle to approximate the joint angle. Both sensors measure acceleration in three dimensions (x, y, and z).

## 1. Code Breakdown
### 1. Library and objects
```C
#include <DFRobot_BMX160.h>
DFRobot_BMX160 bmx160_bicep;
DFRobot_BMX160 bmx160_forearm;
```
- Include the sensor library and create two sensor objects

### 2. Setup
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

### 3. Read sensor data
```C
sBmx160SensorData_t Omagn_b, Ogyro_b, Oaccel_b;
sBmx160SensorData_t Omagn_f, Ogyro_f, Oaccel_f;

bmx160_bicep.getAllData(&Omagn_b, &Ogyro_b, &Oaccel_b);
bmx160_forearm.getAllData(&Omagn_f, &Ogyro_f, &Oaccel_f);
```
- Get data (acceleration, gyroscope, magnetometer) from each sensor
- This code uses acceleration only

### 4. Calculate angle between acceleration vectors
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

### 5. Output data
```C
Serial.print("Elbow Angle: ");
Serial.print(angle_deg);
Serial.println(" degrees\n");
```
- Print the measured angle

## 2. How this works
At rest, the largest static acceleration is from gravity (downward) and all sensors measure this. By comparing the directionality (vector) of gravity detected by each sensor:

- If your arm is straight, both bicep and forearm “sense” gravity in the same direction — angle ≈ 0°
- If you bend your elbow to 90°, the forearm sensor will measure gravity at ~90° relative to the bicep — angle ≈ 90°
- If you bend it fully, ~180°, the sensors will be anti-parallel

The calculation is purely geometric: the angle between the sensors' gravity vectors

## 3. Limitations
- It assumes sensors move as rigid segments with the limb
- Assumes only gravity or slow/static movement; rapid movement or other accelerations can disturb readings
