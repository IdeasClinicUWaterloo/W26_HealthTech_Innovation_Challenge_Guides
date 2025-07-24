To create a database, we will be using sqlalchemy to interact with sqlite, a database storage engine. WTForms will allow us to take user inputs, and Flask helps tie everything together into a web application along with basic HTML and CSS. 
# SQL Database Structures
This content was adapted from [this tutorial](https://realpython.com/python-sqlite-sqlalchemy/#structuring-a-database-with-sql) which can provide more in-depth explanations! 

SQLite is used to create and manage relational databases store data into tables and establish relationships between these tables. Each table have rows of records, and each record is made up of columns/fields which contain data and a primary key which is used as a unique identifier for the record. These primary keys are automatically created as an incrementing integer value by SQLite. 

Relationships can be used to easily group data together even when they’re broken up between different tables. 

One-to-Many relationships are used in this database to relate each exercise session to a patient. One patient can have many different exercise sessions, but each session belongs to only one patient. To establish the one-to-many relationship, within each session record the patient id of the corresponding patient will be stored. These are called foreign keys, and allow for a “lookup” reference back to the unique patient
Many-to-Many relationships are not used in this database, since the personalization of exercise made it difficult to employ effectively. However, if CCCare were to hold exercise classes where all the participants performed the same exercises, we could use many-to-many relationships to connect these classes with the patients. In this case, one class will have multiple patients attending, and one patient can attend multiple classes. These would be established through association tables, where each record contains at least two foreign key fields. Essentially, we combine different primary keys together.

# Using SQLAlchemy 
SQL is the language used to interact with databases, allowing users to create, manage, and query the data. SQLAlchemy is a package which translates between SQL and Python, and Flask-SQLAlchemy lets us use SQLAlchemy inside the context of our web app.
To create our database with SQLAlchemy, we will use models which inherit from a base python class provided by SQLAlchemy that allows for operations between the model and the database table. 
For example, here is the model for the Session table:

```
class Session(db.Model):
    __tablename__ = "sessions"
    session_id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default = False) 
    is_scheduled = db.Column(db.Boolean, default = True) 
    patient_id = db.Column(db.Integer, db.ForeignKey("patient_list.patient_id"))
    cardio_id = db.Column(db.Integer, db.ForeignKey("cardio.cardio_id"))
    mobility_id = db.Column(db.Integer, db.ForeignKey("mobility.mobility_id"))
    squat_lunge_id = db.Column(db.Integer, db.ForeignKey("squat_lunge.squat_lunge_id"))
    push_id = db.Column(db.Integer, db.ForeignKey("push.push_id"))
    pull_id = db.Column(db.Integer, db.ForeignKey("pull.pull_id"))
    hinge_id = db.Column(db.Integer, db.ForeignKey("hinge.hinge_id"))
    carry_id = db.Column(db.Integer, db.ForeignKey("carry.carry_id"))
    core_id = db.Column(db.Integer, db.ForeignKey("core.core_id"))
    stretch_id = db.Column(db.Integer, db.ForeignKey("stretch.stretch_id"))
    heart_rate_id = db.Column(db.Integer, db.ForeignKey("heart_rate.heart_rate_id"))

    patient = db.relationship("Patient", back_populates = "sessions")
```

ForeignKey() defines a dependency between two columns of different tables, establishing a relationship between the tables. For example, `patient_id = db.Column(db.Integer, db.ForeignKey("patient_list.patient_id"))` tells us that there's a column with type Integer in the patient_list table named patient_id and is related to the primary key in the Session table.

relationship() creates a collection by finding the ForeignKey connection point between the two tables

To interact with our database, we need a SQLAlchemy session object. This is not to be confused with the class Session which represents the exercise session model defined within our database. These can be distinguished as the SQLAlchemy session object will always be db.session whereas the model will be capitalized as Session.

If you want to be able to visualize your database, SQLite Viewer is a useful VSCode extension. 

# Flask-WTForms 
WTForms will allow us to take inputs for creating new data or updating existing data. 
Start off by creating forms which mirrors the corresponding model, excluding any fields which don’t require user input. For example, almost all of the exercise types have models defined as such: 
```
class Push(db.Model):
    __tablename__ = "push"
    push_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    reps = db.Column(db.Integer, default = 0)
    target_reps = db.Column(db.Integer)
    weight_lbs = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("push"))
```
However, we wouldn’t want the user to manually define the primary key, and we can implement a method to automatically update the reps completed. Additionally, defining a relationship between tables isn't a field which users can input, so our corresponding form doesn’t include these fields: 
```
class PushForm(FlaskForm):
    exercise_name = StringField('Push Exercise Name')
    target_reps = IntegerField('Target Reps', validators=[Optional()])
    weight_lbs = FloatField('Weight (lbs)', validators=[Optional()])
```

# Breaking down the Flask App
If you want to learn how to create a flask app yourself, [this is a great resource](https://realpython.com/flask-project/) 
Side note: In order to run the app, since the base code is spread across multiple files we use the terminal command `py -m flask --app folder_name_ run --port 8000 –debug` where folder_name is where the code is all stored. 

In the main folder:
### \_\_init\_\_.py
- Initializes the app and returns it
- Activates CSRF token for WTForms to use
- Establishes connection with the database
- Connects blueprint pages to the application
- Starts the serial monitor for the Arduino

### extensions.py
- Initializes the database and SQLAlchemy
- Ensures that only one session will be open, no duplicates

### pages.py
- Creates a blueprint for all the different views within your app
- Defines different routes for each view
- Each route contains code to execute along with rendering the view
    - These involve retrieving relevant data from the database or how to handle form inputs 

In the folder “templates”:
Templates are html files that allow for dynamic displaying with Flask content and can incorporate python-like functionality, such as loops and conditionals.

### base.html
- Main HTML structure for web pages
- Provides consistent structure for other pages
- Empty blocks allow for flexibility in the specific content on each page

### navigation.html
- HTML fragment which is included in base.html
- Focuses only on how to render a navigation menu

In the folder “pages”: 
These are all child templates which extend the base template `base.html`. Each child template fills in the empty blocks of the base template with specific content

### home.html
- Acts as an initial landing page for users

### patients.html
- Displays the patient database in a table
- Uses a for loop to display all patients

### add_patient.html and edit_patient.html
- Corresponding Patient form is passed to the html file
- POST method is used to keep sensitive information private

### sessions.html
- Displays session database in a table
- Accesses the info for each exercise through

### scheduler.html and edit_session.html
- Connects to corresponding Session form and relevant subforms 
