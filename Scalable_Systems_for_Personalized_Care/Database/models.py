from .extensions import db
from sqlalchemy.orm import backref 

class Patient(db.Model):
    __tablename__ = "patient_list"
    patient_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    
    sessions = db.relationship("Session", back_populates = "patient")


class Session(db.Model):
    __tablename__ = "sessions"
    session_id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default = False) # is_active and is_scheduled should be exclusive where both cannot have the same value at the same time
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


class HeartRate(db.Model):
    __tablename__ = "heart_rate"
    heart_rate_id = db.Column(db.Integer, primary_key=True)
    max = db.Column(db.Integer)
    avg = db.Column(db.Integer)
    sessions = db.relationship("Session", backref = backref("heart_rate"))



class Cardio(db.Model):
    __tablename__ = "cardio"
    cardio_id = db.Column(db.Integer, primary_key = True)
    machine_name = db.Column(db.String)
    level = db.Column(db.Integer)
    elevation = db.Column(db.Integer)
    time_min = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("cardio"))

class Mobility(db.Model):
    __tablename__ = "mobility"
    mobility_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    reps = db.Column(db.Integer, default = 0)
    target_reps = db.Column(db.Integer)
    weight_lbs = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("mobility"))

class Squat_Lunge(db.Model):
    __tablename__ = "squat_lunge"
    squat_lunge_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    reps = db.Column(db.Integer, default = 0)
    target_reps = db.Column(db.Integer)
    weight_lbs = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("squat_lunge"))

class Push(db.Model):
    __tablename__ = "push"
    push_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    reps = db.Column(db.Integer, default = 0)
    target_reps = db.Column(db.Integer)
    weight_lbs = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("push"))

class Pull(db.Model):
    __tablename__ = "pull"
    pull_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    reps = db.Column(db.Integer, default = 0)
    target_reps = db.Column(db.Integer)
    weight_lbs = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("pull"))

class Hinge(db.Model):
    __tablename__ = "hinge"
    hinge_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    reps = db.Column(db.Integer, default = 0)
    target_reps = db.Column(db.Integer)
    weight_lbs = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("hinge"))

class Carry(db.Model):
    __tablename__ = "carry"
    carry_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    reps = db.Column(db.Integer, default = 0)
    target_reps = db.Column(db.Integer)
    weight_lbs = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("carry"))

class Core(db.Model):
    __tablename__ = "core"
    core_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    reps = db.Column(db.Integer, default = 0)
    target_reps = db.Column(db.Integer)
    weight_lbs = db.Column(db.Float)
    sessions = db.relationship("Session", backref = backref("core"))

class Stretch(db.Model):
    __tablename__ = "stretch"
    stretch_id = db.Column(db.Integer, primary_key = True)
    exercise_name = db.Column(db.String)
    time_sec = db.Column(db.Integer)
    sessions = db.relationship("Session", backref = backref("stretch"))
