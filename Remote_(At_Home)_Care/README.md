# Remote (At Home) Care
CCCARE aims to expand its programs by offering remote care options for patients. Currently, in-person sessions have limited capacity, and the organization hopes to encourage graduated participants to become more independent while still receiving guidance and support. Additionally, many patients on the waitlist face medical or mobility challenges that prevent them from attending in person — resulting in fewer than 10% of stroke and cancer patients from GRH accessing CCCARE’s services.

By moving toward remote treatment, CCCARE can reach a larger number of patients simultaneously, overcoming space and scheduling constraints. This approach would also help graduates maintain a sense of connection and continuity as they transition to self-directed exercise.

However, CCCARE’s primary concern is ensuring that participants are performing exercises safely, effectively, and in accordance with their prescribed treatment plans.

## The Challenge 
Design a system that ensures patients are completing the correct exercisees and adhering to their treatment plans **at home**.

Here are some things to think about as you come up with solutions for this problem space: How can we combat that feeling of isolation and support them in maintaining their exercise habits? They’ve been used to working out with a group and an instructor, so how do we keep that sense of community going after they’re on their own? 

## Potential Solutions
|Solution Description|Resources Needed|
|:---|:---|
|A mobile or web app that tracks patient movements during remote sessions|<ul> <li> Smartphone or laptop camera <li> [Flask](## "For backend") or [React Native / Flutter](## "For mobile app") <li> [Frontend framework](## "React, Vue, or HTML/CSS/JS") <li> [OpenCV or MediaPipe](## "For body tracking")|
|An AI instructor that gives personalized feedback on form and technique|<ul> <li> [Machine learning model](## "Pose estimation + classification") <li> [Training data](## "Exercise movement datasets") <li> Python + PyTorch / TensorFlow <li> [Motion capture hardware (optional)](## "Camera, accelerometer, IMU sensors")|
|A centralized online platform for live-streamed or pre-recorded exercise sessions|<ul> <li> [Website framework](## "Next.js, React, or Vue") <li> [Backend framework](## "Flask, Django, or Node.js") <li> Video hosting/streaming|

## Resources
- [Machine Vision Guide](./Machine_Vision_Guide.md)
- [Figma_Guide](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/UI_Design/Getting_Started_with_Figma.md)
- [Information on dosages & exercise sessions](https://uofwaterloo.sharepoint.com/:w:/r/sites/tm-eng-engineeringideasclinic/Shared%20Documents/Health%20Hub/W26%20Health%20Tech%20Challenge%202/Dosages%20%26%20Exercise%20Sessions%20-%20More%20Details.docx?d=w4848032b80e54a9bab7b14fe89a329c8&csf=1&web=1&e=g0tvef)
