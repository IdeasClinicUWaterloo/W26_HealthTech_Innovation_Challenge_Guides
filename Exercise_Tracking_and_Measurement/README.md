# Exercise Tracking and Measurement
In CCCARE, each instructor typically supervises 10–12 participants per session, while sessions for graduated participants may include up to 30 individuals per instructor. With such limited supervision, it becomes challenging to monitor each participant’s exercise performance accurately. As a result, some participants may fail to complete their prescribed exercise dose, while others may exceed it, potentially leading to inconsistent outcomes.

Student volunteers are available to assist participants who need additional support—such as individuals recovering from stroke or those living with dementia. However, since not every participant has access to a one-on-one volunteer, there is a clear need for a system that can track and assess the quality of exercises performed. Such a system would allow instructors to evaluate participant progress, ensure exercise adherence, and maintain consistent quality across sessions.

## The Challenge
Design a system that **tracks** and **measures** the quality of patient activity. 

## Potential Solutions
|Potential Solutions|Resources Needed|
|:---|:---|
|Motion trackers that are worn on the wrist/ankle (like a fitness tracker) to track limb motion, speed, and tremor|<ul> <li> [Accelerometers](## "Measures angle and position") <li> [Arduino](## "Reads data from the sensors") <li> [3d printed attachment/frame](## "Mounts hardware to the body")|
|A vest that can be worn during exercise to track vitals (like smart clothes), such as heart rate, heart rate variability, breathing rate/volume|<ul> <li> [Oximeter](## "Senses heart rate and blood oxygen") <li> Various sensors <li> [Arduino](## "Reads inputs from sensors") <li> Vest|
|Exercise mats (or step platforms) or wearable equipment embedded with pressure sensors to detect movement, force, and repetitions|<ul> <li> [Pressure sensors](## "Detect pressure") <li> Various sensors (i.e. [accelerometers](## "Detects movement")) <li> [Arduino](## "Reads inputs from sensors") <li> Exercise mats/step platform|
|Add sensors to existing exercise equipment|<ul> <li> Various sensors <li> Exercise equipment to be modified|

<!--
- Motion trackers that are worn on the wrist/ankle (like a fitness tracker) to track limb motion, speed, and tremor
- A vest that can be worn during exercise to track vitals (like smart clothes) such as heart rate, heart rate variability, breathing rate/volume
- Exercise mats (or step platforms) or wearable equipment embedded with pressure sensors to detect movement, force, and repetitions
- Add sensors to existing exercise equipment
-->

## Resources
- [Tutorial on 3D printing](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/IdeasClinicUWaterloo-patch-1/3D_Modeling_and_Printing/GUIDE.md)
- [Tutorial on implementing dual accelerometers](./Sensor/Dual_Accelerometers_for_Exercise_Tracking.md)
- [Other sensors](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/IdeasClinicUWaterloo-patch-1/Sensors/GUIDE.md)
- [Arduino Introduction Tutorial](https://learn.uwaterloo.ca/d2l/le/content/1017258/viewContent/6055337/View)
- [Information on dosages & exercise sessions](https://uofwaterloo.sharepoint.com/:w:/r/sites/tm-eng-engineeringideasclinic/_layouts/15/Doc.aspx?sourcedoc=%7B4848032B-80E5-4A9B-AB7B-14FE89A329C8%7D&file=Dosages%20&%20Exercise%20Sessions%20-%20More%20Details.docx=&action=default&mobileredirect=true)
