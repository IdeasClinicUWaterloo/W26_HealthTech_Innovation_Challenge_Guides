# Exercise Tracking and Measurement
In CCCARE, each instructor typically supervises 10–12 participants per session, while sessions for graduated participants may include up to 30 individuals per instructor. With such limited supervision, it becomes challenging to monitor each participant’s exercise performance accurately. As a result, some participants may fail to complete their prescribed exercise dose, while others may exceed it, potentially leading to inconsistent outcomes.

Student volunteers are available to assist participants who need additional support—such as individuals recovering from stroke or those living with dementia. However, since not every participant has access to a one-on-one volunteer, there is a clear need for a system that can track and assess the quality of exercises performed. Such a system would allow instructors to evaluate participant progress, ensure exercise adherence, and maintain consistent quality across sessions.

## The Challenge
Design a system that **tracks** and **measures** the quality of patient activity. 

## Potential Solutions
|Solution Description|Resources Needed|
|:---|:---|
| Motion trackers that are worn on the wrist/ankle (like a fitness tracker) to track limb motion, speed, and tremor | <ul><li>Accelerometers (measure angle and position)</li><li>Arduino (reads data from the sensors)</li><li>3D printed attachment/frame (mounts hardware to the body)</li></ul> |
| A vest that can be worn during exercise to track vitals (like smart clothes), such as heart rate, heart rate variability, breathing rate/volume | <ul><li>Oximeter (senses heart rate and blood oxygen)</li><li>Various sensors</li><li>Arduino (reads inputs from sensors)</li><li>Vest</li></ul> |
| Exercise mats (or step platforms) or wearable equipment embedded with pressure sensors to detect movement, force, and repetitions | <ul><li>Pressure sensors (detect pressure)</li><li>Various sensors (e.g., accelerometers for movement detection)</li><li>Arduino (reads inputs from sensors)</li><li>Exercise mats/step platform</li></ul> |
| Add sensors to existing exercise equipment | <ul><li>Various sensors</li><li>Exercise equipment to be modified</li></ul> |

## Resources
- [Tutorial on 3D printing](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/3D_Modeling_and_Printing/GUIDE.md)
- [Tutorial on implementing dual accelerometers for exercise tracking](./Sensor/Dual_Accelerometers_for_Exercise_Tracking.md)
- [Other sensors](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Sensors/GUIDE.md)
- [Arduino Introduction Tutorial](https://github.com/IdeasClinicUWaterloo/TechResources/blob/main/Arduino/GUIDE.md)
- [Information on dosages & exercise sessions](https://uofwaterloo.sharepoint.com/:w:/r/sites/tm-eng-engineeringideasclinic/_layouts/15/Doc.aspx?sourcedoc=%7B4848032B-80E5-4A9B-AB7B-14FE89A329C8%7D&file=Dosages%20&%20Exercise%20Sessions%20-%20More%20Details.docx=&action=default&mobileredirect=true)
