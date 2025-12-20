# this is just for using info from the Arduino
import threading
import serial
from datetime import date
import time
import numpy as np
from collections import deque

from .models import Session, Pull, Push
from .extensions import db


print("Listening for IMU data...")

def read_sensor_loop(app):
    PORT = 'COM7'  # Change this to match whichever port Arduino is connected to 
    BAUD = 115200
    pressed = 0

    # Parameters
    WINDOW_SIZE = 50
    sen1_motion_score_buf = deque(maxlen=WINDOW_SIZE)
    sen2_motion_score_buf = deque(maxlen=WINDOW_SIZE)
    sen1_rep_count = 0
    sen2_rep_count = 0

    # Peak detection state
    cooldown = 0.5  # seconds between reps
    last_rep_time = time.time()
    total_time = 0
    peak1= False
    peak2 = False
    pace_left = 0
    pace_right = 0

    # Thresholds
    MOTION_THRESHOLD = 80 # signal must go above this to count as movement (can adjust based on motion pattern)
    FALL_THRESHOLD = 20    # signal must drop below this to reset

    with app.app_context(): #ensures this occurs within the flask app
        ser = serial.Serial(PORT, BAUD, timeout=1) # setup serial connection
        while True: 
            try:
                # take in the sensor data coming from Arduino
                line = ser.readline().decode().strip() #reads the incoming data
                values = list(map(float, line.split(','))) #turns the data into a list of floats using the , to determine where to split
                if len(values) != 13: #check that the correct number of values were received, break from the loop if not
                    print("incorrect formatting: ", line)
                    continue
                
                #Check if session is currently active, and (ideally) what exercise they are on
                exercise = None
                current_session = db.session.query(Session).filter_by(is_active=True).first()
                #THIS CODE IS FLAWED, just testing to see if it was possible to continue or create a new exercise record
                #ideally there would be a way to determine what exercise the patient is currently working on
                if current_session and current_session.push_id:
                    exercise = db.session.query(Push).filter_by(push_id=current_session.push_id).first()

                # If no valid session or exercise, make a new one
                if not current_session or not exercise:
                    #if no current active session, marks any sessions as not active
                    db.session.query(Session).filter_by(is_active=True).update({'is_active': False}) 
                    db.session.commit()
                    #creates a new exercise record (with these set values for now, but does not have to be)
                    push = Push(exercise_name="Chest Press", reps=0, target_reps=12, weight_lbs=27.5)
                    db.session.add(push)
                    db.session.commit()
                    #creates a new session, marks it as active, and assigns the newly created exercise record to itself
                    new_session = Session(is_active=True, is_scheduled=False, date=date.today(), push_id=push.push_id)
                    db.session.add(new_session)
                    db.session.commit()

                    current_session = new_session
                    exercise = push

                #assign the incoming values from the Arduino to these variables
                pressed, a1x_, a1y_, a1z_, g1x_, g1y_, g1z_, a2x_, a2y_, a2z_, g2x_, g2y_, g2z_ = values
                #calculate a "motion score" for each sensor
                accel_mag1 = np.sqrt(a1x_**2 + a1y_**2 + a1z_**2)
                gyro_mag1 = np.sqrt(g1x_**2 + g1y_**2 + g1z_**2)
                motion_score1 = accel_mag1 + gyro_mag1
        
                accel_mag2 = np.sqrt(a2x_**2 + a2y_**2 + a2z_**2)
                gyro_mag2 = np.sqrt(g2x_**2 + g2y_**2 + g2z_**2)
                motion_score2 = accel_mag2 + gyro_mag2
                # get the current time 
                current_time = time.time()
                # append the motion score to the buffer list
                sen1_motion_score_buf.append(motion_score1)
                sen2_motion_score_buf.append(motion_score2)

                #if we're not already within a peak (motion score has not dropped below fall threshold), motion score qualifies as a peak,
                # and the touch sensor reads high, then we increase the number of repitions and recalculate the repetition pace 
                if not peak1 and motion_score1 > MOTION_THRESHOLD and pressed:
                    peak1= True #indiate that we are in a peak
                    sen1_rep_count += 1 #increase the number of repetitions
                    total_time+= (current_time - last_rep_time) #increase the amount of time repetitions have taken
                    last_rep_time = current_time 
                    pace_left = total_time/sen1_rep_count #pace in seconds per rep
                    print(f"💪 Left Rep #{sen1_rep_count} at {pace_left:.2f} sec/rep    STOPWATCH: {total_time:.2f}")

                # Reset peak detection when the signal falls back below the fall threshold
                elif peak1 and motion_score1 < FALL_THRESHOLD:
                    peak1 = False

                if not peak2 and motion_score2 > MOTION_THRESHOLD and pressed:
                    peak2= True 
                    sen2_rep_count += 1
                    total_time+= (current_time - last_rep_time)
                    last_rep_time = current_time

                    pace_right = total_time/sen2_rep_count #pace in seconds per rep
                    print(f"💪 Right Rep #{sen2_rep_count} at {pace_right:.2f} sec/rep    STOPWATCH: {total_time:.2f}")

                elif peak2 and motion_score2 < FALL_THRESHOLD:
                    peak2 = False

                #only update the database with the rep count if both counts are the same 
                if sen1_rep_count == sen2_rep_count:
                    exercise.reps = sen1_rep_count
                    db.session.commit()

                
            except KeyboardInterrupt:
                print("Stopped by user.")
                break
            except Exception as e:
                print("Error:", e)
                continue

# thread to allow for the use of serial port as the app is running
def start_serial_thread(app):
    thread = threading.Thread(target=read_sensor_loop, args=(app,), daemon=True)
    thread.start()
