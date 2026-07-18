# Exercise Tracking and Measurement
At CCCARE, each instructor typically supervises 10–12 participants per session. Sessions for graduated participants may include up to 30 participants per instructor.

With limited supervision, it can be difficult to accurately monitor each participant's exercise performance. As a result:

- Some participants may not complete their prescribed exercises.
- Others may perform more repetitions than recommended.
- Exercise quality and participant outcomes may become inconsistent.

Student volunteers are available to support participants who need additional assistance, such as individuals recovering from a stroke or living with dementia. However, because one-on-one support is not available for every participant, there is a need for a system that can monitor exercise performance consistently.

A tracking system would help instructors:

- Monitor participant progress.                                                                         
- Measure exercise quality.
- Ensure participants complete the correct exercise dose.
- Support consistent instruction across all sessions.

  <img width="230" height="220" alt="Measure Training" src="https://github.com/user-attachments/assets/e4cbe7ee-89be-4e95-89bf-f596444dc09d" />
  <img width="240" height="220" alt="Smart Vest" src="https://github.com/user-attachments/assets/cb59314e-16a3-4318-90af-0a578c2f8bdc" />


## The Challenge
Design a system that **tracks** and **measures** the quality of patient activity. 

## Potential Solutions
The ideas below are examples to help you get started. You may choose one of these ideas or combine multiple approaches if appropriate.

| **Potential Solution** | **Resources Needed** |
|:-----------------------|:---------------------|
| **Wearable Motion Tracker**<br>Develop a wrist- or ankle-worn device (similar to a fitness tracker) that monitors limb movement, speed, and tremors during exercise. | <ul><li>Accelerometers (measure angle and position)</li><li>Arduino (reads data from the sensors)</li><li>3D-printed attachment/frame (mounts hardware to the body)</li></ul> | 
| **Smart Exercise Vest**<br>Design a wearable vest that tracks vital signs during exercise, such as heart rate, heart rate variability, breathing rate, and breathing volume. | <ul><li>Pulse oximeter (measures heart rate and blood oxygen)</li><li>Various sensors</li><li>Arduino (reads inputs from sensors)</li><li>Vest</li></ul> |
| **Pressure-Sensing Exercise Mat or Step Platform**<br>Develop an exercise mat, step platform, or wearable device with embedded pressure sensors to detect movement, force, and exercise repetitions. | <ul><li>Pressure sensors (detect pressure)</li><li>Various sensors (e.g., accelerometers for movement detection)</li><li>Arduino (reads inputs from sensors)</li><li>Exercise mat or step platform</li></ul> |
| **Sensor-Enhanced Exercise Equipment**<br>Modify existing exercise equipment by adding sensors that automatically measure exercise performance. | <ul><li>Various sensors</li><li>Existing exercise equipment to be modified</li></ul> |


## Resources
- [Tutorial on 3D printing](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/3D_Modeling_and_Printing/GUIDE.md)
- [Tutorial on implementing dual accelerometers for exercise tracking](./Sensor/Dual_Accelerometers_for_Exercise_Tracking.md)
- [Other sensors](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Sensors/GUIDE.md)
- [Arduino Introduction Tutorial](https://github.com/IdeasClinicUWaterloo/TechResources/blob/main/Arduino/GUIDE.md)
- [Information on dosages & exercise sessions](https://uofwaterloo.sharepoint.com/:w:/r/sites/tm-eng-engineeringideasclinic/_layouts/15/Doc.aspx?sourcedoc=%7B4848032B-80E5-4A9B-AB7B-14FE89A329C8%7D&file=Dosages%20&%20Exercise%20Sessions%20-%20More%20Details.docx=&action=default&mobileredirect=true)
