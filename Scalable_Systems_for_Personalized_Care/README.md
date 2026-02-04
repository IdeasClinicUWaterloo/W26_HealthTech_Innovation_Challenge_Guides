# Scalable Systems for Personalized Care
At CCCARE, each participant receives a personalized exercise plan—referred to as a dosage—that specifies the type and amount of physical activity best suited to their individual needs. These plans are continuously adjusted based on progress and feedback.

Initial assessments are performed by Kinesiologists and other rehabilitation professionals, who determine each participant’s starting point by evaluating their physical ability, medical history, and personal goals. To ensure that adjustments are effective, instructors must be able to easily access and review each patient’s exercise history and performance data.

Currently, CCCARE relies on a hybrid data management system combining both digital and paper-based methods:
- exercise logs are stored on paper
- appointments are scheduled using AirTable
- intake assessments are written on paper and manually input into a Microsoft Access database by staff
- referrals from the Waterloo Regional Health Network (WRHN) are sent in by fax which requires manual entry into the database
  
Unfortunately, Access cannot be integrated with other clinical software or visualize data, hindering data sharing and coordination.

## The Challenge
Design a **scalable** system that makes it easier to prescribe, adjust, store, and share exercise doses efficiently.

## Potential Solutions
|Solution Description|Resources Needed|
|:---|:---|
| A database that can add, remove, and update each patient individually | <ul><li>Database system (SQLite (local), PostgreSQL/MySQL (production), or Firebase)</li><li>Backend framework (Flask, Django, or Node.js)</li><li>ORM (SQLAlchemy, Django ORM, or Prisma)</li><li>API endpoints for CRUD operations (Create, Read, Update, Delete)</li><li>Cloud hosting (AWS, Azure, Render, or Railway)</li></ul> |
| A portable assessment “toolkit” with simple mechanical tests (with sensors) to help professionals gather patient metrics | <ul><li>Mechanical assessment tool</li><li>Sensors (for digital measurement)</li><li>3D-printed parts</li><li>Data collection app</li><li>UI/UX design (Figma)</li></ul> |
| A dashboard for instructors to log progress and easily transfer notes | <ul><li>Website framework (Next.js, React, or Vue)</li><li>Database for storing logs, notes, and patient progress</li><li>Note-taking components</li><li>Progress visualization</li><li>File upload support</li><li>UI/UX design (Figma)</li></ul> |

## Resources
- [Tutorial on how to create a SQLAlchemy-based SQL database](./SQL_Database_Guide.md)
- [Sensors Guide](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/Sensors/GUIDE.md)
- [Information on dosages & exercise sessions](https://uofwaterloo.sharepoint.com/:w:/r/sites/tm-eng-engineeringideasclinic/Shared%20Documents/Health%20Hub/W26%20Health%20Tech%20Challenge%202/Dosages%20%26%20Exercise%20Sessions%20-%20More%20Details.docx?d=w4848032b80e54a9bab7b14fe89a329c8&csf=1&web=1&e=g0tvef)
- [Figma Guide](https://github.com/IdeasClinicUWaterloo/Technologies-Utilized-for-Idea-s-Clinic-Challenges/blob/main/UI_Design/Getting_Started_with_Figma.md)
