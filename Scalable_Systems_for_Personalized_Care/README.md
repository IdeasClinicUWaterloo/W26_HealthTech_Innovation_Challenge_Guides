# Scalable Systems for Personalized Care
At CCCARE, each participant receives a personalized exercise plan—referred to as a dosage—that specifies the type and amount of physical activity best suited to their individual needs. These plans are continuously adjusted based on progress and feedback.

Initial assessments are performed by Kinesiologists and other rehabilitation professionals, who determine each participant’s starting point by evaluating their physical ability, medical history, and personal goals. To ensure that adjustments are effective, instructors must be able to easily access and review each patient’s exercise history and performance data.

Currently, CCCCARE relies on a hybrid data management system combining both digital and paper-based methods:
- exercise logs are stored on paper
- appointments are scheduled using AirTable
- intake assessments are written on paper and manually input into a Microsoft Access database by staff
- referrals from the Waterloo Regional Health Network (WRHN) are sent in by fax which requires manual entry into the database
  
Unfortunately, Access cannot be integrated with other clinical software or visualize data, hindering data sharing and coordination.

More information on dosages & exercise sessions can be found [here](https://uofwaterloo.sharepoint.com/:w:/r/sites/tm-eng-engineeringideasclinic/Shared%20Documents/Health%20Hub/W26%20Health%20Tech%20Challenge%202/Dosages%20%26%20Exercise%20Sessions%20-%20More%20Details.docx?d=w4848032b80e54a9bab7b14fe89a329c8&csf=1&web=1&e=g0tvef)

## The Challenge
Design a **scalable** system that makes it easier to prescribe, adjust, store, and share exercise doses efficiently.

## Potential Solutions
- A database that can add, remove, and update each patient individually
- A portable assessment “toolkit” with simple mechanical tests (w/ sensors) to aid professionals quickly gather the patient’s metrics for prescription 
- A dashboard for instructors to log progress and easily transfer notes. 

## Resources
- [Tutorial on how to create a database](./SQL_Database_Guide.md)
- [Documentation of Definitions of terms used by CCCare](https://uofwaterloo.sharepoint.com/:w:/r/sites/tm-eng-engineeringideasclinic/_layouts/15/Doc.aspx?sourcedoc=%7B4848032B-80E5-4A9B-AB7B-14FE89A329C8%7D&file=Dosages%20&%20Exercise%20Sessions%20-%20More%20Details.docx=&action=default&mobileredirect=true)
