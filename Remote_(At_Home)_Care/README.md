# Remote (At Home) Care

## Background

CCCARE currently provides supervised rehabilitation programs for stroke and cancer patients. However, in-person sessions have limited capacity, and many patients are unable to attend due to medical or mobility challenges.

To expand access, CCCARE aims to introduce remote (at-home) rehabilitation programs that allow patients to continue exercising safely while receiving guidance and support.

> **Less than 10% of stroke and cancer patients referred from GRH currently access CCCARE's services.**

Remote care has the potential to improve accessibility, reduce scheduling constraints, and help graduates maintain continuity after completing in-person programs.

---

## The Challenge

Design a remote rehabilitation system that helps patients:

- Perform the correct exercises
- Follow their prescribed treatment plans
- Exercise safely without direct supervision
- Stay motivated and connected while exercising at home

### Design Considerations

Consider questions such as:

- How can patients receive meaningful feedback without an instructor physically present?
- How can the system detect incorrect movements or unsafe exercises?
- How can we encourage long-term adherence to rehabilitation programs?
- How can we recreate the sense of community from in-person sessions?

---

## Potential Solutions
|Solution Description|Resources Needed|
|:---|:---|
|A mobile or web app that tracks patient movements during remote sessions|<ul><li> Camera (smartphone or laptop) <li> Backend web (Flask) or Mobile app (React Native / Flutter) <li> Frontend framework (React, Vue, HTML/CSS/JS, or Figma) <li> OpenCV or MediaPipe (body tracking libraries)</ul>|
|An AI instructor that gives personalized feedback on form and technique|<ul><li> Machine learning model (pose estimation + classification) <li> Training data (exercise movement datasets) <li> Python with PyTorch/TensorFlow <li> Motion capture hardware (optional: camera, accelerometer, IMU sensors)</ul>|
|A centralized online platform for live-streamed or pre-recorded exercise sessions|<ul><li> Website framework (Next.js, React, Vue, or Figma) <li> Backend framework (Flask, Django, or Node.js) <li> Video hosting or streaming services</ul>

---

## Resources
- [Machine Vision Guide](./Machine_Vision_Guide.md)
- [Figma Guide](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/UI_Design/Getting_Started_with_Figma.md)
- [Information on dosages & exercise sessions](https://uofwaterloo.sharepoint.com/:w:/r/sites/tm-eng-engineeringideasclinic/Shared%20Documents/Health%20Hub/W26%20Health%20Tech%20Challenge%202/Dosages%20%26%20Exercise%20Sessions%20-%20More%20Details.docx?d=w4848032b80e54a9bab7b14fe89a329c8&csf=1&web=1&e=g0tvef)
