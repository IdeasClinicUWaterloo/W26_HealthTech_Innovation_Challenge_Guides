from flask import Blueprint, render_template, redirect, url_for

from .extensions import db
from .models import Session, Patient, Cardio, Mobility, Squat_Lunge, Push, Pull, Hinge, Carry, Core, Stretch 
from .forms import SessionForm, PatientForm, DeleteForm

bp = Blueprint("pages", __name__)

#default landing page
@bp.route("/") # this associates the URL "/" with the home function
def home(): # the function is called whenever a request to our server home page is received
    return render_template("pages/home.html") #specifies which html file to load

#page displaying patient list
@bp.route("/patients", endpoint = "patients") #endpoint can be used to ensure the page is routing correctly, should be the same name as the function to be called
def patients():
    patients = db.session.query(Patient).all() #retrieves all patients stored in the database and attaches to an object
    return render_template("pages/patients.html", patients = patients) #object is passed to the html file and referenced in for loop to add table entries  

#page displaying session database
@bp.route("/session_list")
def session_list():
    sessions = db.session.query(Session).all() # retrieves all instances of sessions stored in database and attaches to an object
    delete_forms = {s.session_id: DeleteForm() for s in sessions} #creates a deleteform for each session in database and attaches to an object
    return render_template("pages/sessions.html", sessions=sessions, delete_forms = delete_forms) # sessions object and delete form object is passed to html file

#page for creating a new patient in the database 
@bp.route("/add_patient", methods = ["GET", "POST"]) #get and post methods can be used to retrieve and send data
def add_patient():
 # this happens before the page is rendered
    form = PatientForm() #creates a form 

 # this happens after the page is rendered and form is submitted
    if form.validate_on_submit(): #only creates a new patient if all required fields have appropriate data entered in once submitted
        patient = Patient(first_name = form.first_name.data, last_name = form.last_name.data) #create a new patient instance with submitted data
        db.session.add(patient) #sends the new patient to the database to be stored
        db.session.commit() #finalizes the "transaction" and makes sure the change is permanent and visible to all users
        return redirect(url_for("pages.patients")) #after patient has been stored, redirect to the patient list page
        #url_for() is used to ensure correct path
    return render_template("pages/add_patient.html", form = form) # pass form object to html file 

#page for editing the info about a patient
@bp.route("/edit_patient/<int:patient_id>", methods = ["GET", "POST"]) #url has an int variable, used to pass patient_id to the function
def edit_patient(patient_id): 
    patient = Patient.query.get_or_404(patient_id) #retrieves the relevant patient from primary key (patient_id), returns 404 page if there's nothing to retrieve
    form = PatientForm(obj=patient) #creates a patient form with the current patient info already filled in
    
    if form.validate_on_submit(): 
        patient.first_name = form.first_name.data #assign newly submitted data to patient info in database
        patient.last_name = form.last_name.data
        db.session.commit() #finalizes the changes
        return redirect(url_for("pages.patients")) #after patient info has been updated, redirect to patient list page
    
    return render_template("pages/edit_patient.html", patient = patient, form = form) # pass form and patient object to html file for proper rendering
    
# page for creating a new session in the database
@bp.route("/session_scheduling", methods = ["GET", "POST"])
def session_scheduling():
    form = SessionForm() # create a SessionForm object
    form.populate_patient_choices() # run function to retrieve a list of sorted patients for drop down menu

    if form.validate_on_submit(): # only creates a new Session record if all required fields as filled
        cardio = Cardio() # create a Cardio record
        form.cardio.form.populate_obj(cardio) # fill the Cardio record with data submitted in form
        # accessing the cardio subform in the SessionForm object (form.cardio.form)
        #repeat for all other exercise subforms
        mobility = Mobility()
        form.mobility.form.populate_obj(mobility)
        squat_lunge = Squat_Lunge()
        form.squat_lunge.form.populate_obj(squat_lunge)
        push = Push()
        form.push.form.populate_obj(push)
        pull = Pull()
        form.pull.form.populate_obj(pull)
        hinge = Hinge()
        form.hinge.form.populate_obj(hinge)
        carry = Carry()
        form.carry.form.populate_obj(carry)
        core = Core()
        form.core.form.populate_obj(core)
        stretch = Stretch()
        form.stretch.form.populate_obj(stretch)
        # add the records for all exercises to their respective tables to assign exercise IDs before linking in Session
        db.session.add_all([cardio, mobility, squat_lunge, push, pull, hinge, carry, core, stretch])
        db.session.flush()  # flush sends all pending changes to the database, not yet committed

        session = Session( # create a session data, assigning all appropriate exercise ids and other data from the form
            date=form.date.data,
            patient_id=form.patient.data,
            cardio_id = cardio.cardio_id,
            mobility_id = mobility.mobility_id,
            squat_lunge_id = squat_lunge.squat_lunge_id,
            push_id=push.push_id,
            pull_id=pull.pull_id,
            hinge_id = hinge.hinge_id,
            carry_id = carry.carry_id,
            core_id = core.core_id,
            stretch_id = stretch.stretch_id
        )
        db.session.add(session) # add the Session record to the database
        db.session.commit() # finalize all changes
    
        return redirect(url_for("pages.session_list")) # render the page which displays the Session database
    
    return render_template("pages/scheduler.html", form = form)

# define a helper function to be used below by
# filling out the information already stored into the created form
def populate(form, form_field, session, session_field, Model): 
    if hasattr(form, form_field): # checks if the subform exists in the main form
        if getattr(session, session_field) is None: # if the session doesn't already have a corresponding record for the exercise
            setattr(session, session_field, Model()) # create a new record of the exercise model
        getattr(form, form_field).form.populate_obj(getattr(session, session_field)) # assign user submitted info to the exercise record
# page for editing the info in a session record
@bp.route("/edit_session/<int:session_id>", methods=["GET", "POST"])
def edit_session(session_id):
    session = Session.query.get_or_404(session_id) #retrieve the Session through the primary key (session_id) and redirects to 404 page if unable to find it
    form = SessionForm(obj=session) #creates a Session form with the current session info already filled in 

    form.populate_patient_choices() #retrieves the patient list for the dropdown menu

    if form.validate_on_submit(): # (re)assigns user submitted data to the exercise records
        session.date = form.date.data 
        if hasattr(form, 'patient'):
            session.patient = db.session.get(Patient, form.patient.data)
        populate(form, 'cardio', session, 'cardio', Cardio)
        populate(form, 'mobility', session, 'mobility', Mobility)
        populate(form, 'squat_lunge', session, 'squat_lunge', Squat_Lunge)
        populate(form, 'push', session, 'push', Push)
        populate(form, 'pull', session, 'pull', Pull)
        populate(form, 'hinge', session, 'hinge', Hinge)
        populate(form, 'carry', session, 'carry', Carry)
        populate(form, 'core', session, 'core', Core)
        populate(form, 'stretch', session, 'stretch', Stretch)
        db.session.commit()
        return redirect(url_for("pages.session_list", session_id=session_id))

    return render_template("pages/edit_session.html", form=form, session=session)


# there is not an html page to be rendered here, but this allows for functionality to delete a session
@bp.route("/delete_session/<int:session_id>", methods=["POST"])
def delete_session(session_id):
    session = Session.query.get_or_404(session_id) #retrieve the Session
    
    # delete related exercise records first 
    if session.cardio:
        db.session.delete(session.cardio)
    if session.mobility:
        db.session.delete(session.mobility)
    if session.squat_lunge:
        db.session.delete(session.squat_lunge)
    if session.push:
        db.session.delete(session.push)
    if session.pull:
        db.session.delete(session.pull)
    if session.hinge:
        db.session.delete(session.hinge)
    if session.carry:
        db.session.delete(session.carry)
    if session.core:
        db.session.delete(session.core)
    if session.stretch:
        db.session.delete(session.stretch)
    
    db.session.delete(session) # delete the session record
    db.session.commit() 
    return redirect(url_for("pages.session_list"))  # directly displays Session display
