#include <DFRobot_BMX160.h>

DFRobot_BMX160 bmx160_bicep; // Sensor 1 on bicep (default I2C: 0x68)
DFRobot_BMX160 bmx160_forearm; // Sensor 2 on forearm (ADDR pin HIGH: 0x69)

void setup() {
Serial.begin(115200);
delay(100);

// Initialize bicep sensor (I2C address 0x68)
if (bmx160_bicep.begin(0x68) != true) {
Serial.println("Bicep sensor init failed!");
while (1);
}

// Initialize forearm sensor (I2C address 0x69)
if (bmx160_forearm.begin(0x69) != true) {
Serial.println("Forearm sensor init failed!");
while (1);
}

delay(100);
}

void loop() {
sBmx160SensorData_t Omagn_b, Ogyro_b, Oaccel_b;
sBmx160SensorData_t Omagn_f, Ogyro_f, Oaccel_f;

// Read all data from both sensors
bmx160_bicep.getAllData(&Omagn_b, &Ogyro_b, &Oaccel_b);
bmx160_forearm.getAllData(&Omagn_f, &Ogyro_f, &Oaccel_f);

// Calculate dot product and magnitudes of acceleration vectors
float dot = Oaccel_b.x * Oaccel_f.x + Oaccel_b.y * Oaccel_f.y + Oaccel_b.z * Oaccel_f.z;
float mag_b = sqrt(Oaccel_b.x * Oaccel_b.x + Oaccel_b.y * Oaccel_b.y + Oaccel_b.z * Oaccel_b.z);
float mag_f = sqrt(Oaccel_f.x * Oaccel_f.x + Oaccel_f.y * Oaccel_f.y + Oaccel_f.z * Oaccel_f.z);

// Avoid division by zero
float angle_deg = 0;
if (mag_b > 0 && mag_f > 0) {
float angle_rad = acos(dot / (mag_b * mag_f));
angle_deg = angle_rad * 180.0 / PI;
}

// Output sensor data and calculated angle
Serial.println("=== BICEP SENSOR ===");
Serial.print("Accel: X: "); Serial.print(Oaccel_b.x); Serial.print(" ");
Serial.print("Y: "); Serial.print(Oaccel_b.y); Serial.print(" ");
Serial.print("Z: "); Serial.println(Oaccel_b.z);

Serial.println("=== FOREARM SENSOR ===");
Serial.print("Accel: X: "); Serial.print(Oaccel_f.x); Serial.print(" ");
Serial.print("Y: "); Serial.print(Oaccel_f.y); Serial.print(" ");
Serial.print("Z: "); Serial.println(Oaccel_f.z);

Serial.print("Elbow Angle: ");
Serial.print(angle_deg);
Serial.println(" degrees\n");

delay(500);
}
