from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateField, SelectField, SubmitField, FormField 
from wtforms.validators import DataRequired, Optional
from .models import Patient, Cardio, Mobility, Squat_Lunge, Push, Pull, Hinge, Carry, Core, Stretch

class DeleteForm(FlaskForm):
    submit = SubmitField("Delete")

#sub-forms to fill out info in the different tables for each exercise category  
class CardioForm(FlaskForm):
    # each line creates an entry field for users to fill out
    machine_name = StringField('Cardio Machine')
    level = IntegerField('Level', validators=[Optional()])
    elevation = IntegerField('Elevation', validators=[Optional()])
    time_min = FloatField('Time (minutes)', validators=[Optional()])

class MobilityForm(FlaskForm):
    exercise_name = StringField('Mobility Exercise Name')
    target_reps = IntegerField('Target Reps', validators=[Optional()])
    weight_lbs = FloatField('Weight (lbs)', validators=[Optional()])

class SquatLungeForm(FlaskForm):
    exercise_name = StringField('Squat/Lunge Exercise Name')
    target_reps = IntegerField('Target Reps', validators=[Optional()])
    weight_lbs = FloatField('Weight (lbs)', validators=[Optional()])

class PushForm(FlaskForm):
    exercise_name = StringField('Push Exercise Name')
    target_reps = IntegerField('Target Reps', validators=[Optional()])
    weight_lbs = FloatField('Weight (lbs)', validators=[Optional()])

class PullForm(FlaskForm):
    exercise_name = StringField('Pull Exercise Name')
    target_reps = IntegerField('Target Reps', validators=[Optional()])
    weight_lbs = FloatField('Weight (lbs)', validators=[Optional()])

class HingeForm(FlaskForm):
    exercise_name = StringField('Hinge Exercise Name')
    target_reps = IntegerField('Target Reps', validators=[Optional()])
    weight_lbs = FloatField('Weight (lbs)', validators=[Optional()])

class CarryForm(FlaskForm):
    exercise_name = StringField('Carry Exercise Name')
    target_reps = IntegerField('Target Reps', validators=[Optional()])
    weight_lbs = FloatField('Weight (lbs)', validators=[Optional()])

class CoreForm(FlaskForm):
    exercise_name = StringField('Core Exercise Name')
    target_reps = IntegerField('Target Reps', validators=[Optional()])
    weight_lbs = FloatField('Weight (lbs)', validators=[Optional()])

class StretchForm(FlaskForm):
    exercise_name = StringField('Stretch  Name')
    time_sec = FloatField('Time (seconds)', validators=[Optional()])

# main form for creating a session
class SessionForm(FlaskForm):
    date = DateField('Session Date', validators=[DataRequired()])
    patient = SelectField('Patient', coerce=int, validators=[DataRequired()]) 
    # this creates a drop down menu for users to select patients
    # coerce=int is used to obtain the corresponding patient id
    
    # FormField allows for each subform to be included
    cardio = FormField(CardioForm)
    mobility = FormField(MobilityForm)
    squat_lunge = FormField(SquatLungeForm)
    push = FormField(PushForm)
    pull = FormField(PullForm)
    hinge = FormField(HingeForm)
    carry = FormField(CarryForm)
    core = FormField(CoreForm)
    stretch = FormField(StretchForm)
    submit = SubmitField('Schedule Session') 
    # function to retrieve all of the patients in the database
    def populate_patient_choices(self):
        self.patient.choices = [(p.patient_id, f"{p.first_name} {p.last_name} (ID: {p.patient_id})") for p in Patient.query.all()]

class PatientForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    submit = SubmitField('Add Patient')