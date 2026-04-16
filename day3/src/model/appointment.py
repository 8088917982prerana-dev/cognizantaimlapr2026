from datetime import time
from doctor import doctor
from patient import patient
class appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
    def __str__(self):
        return f"Appointment {self.appointment_id} for {self.patient.name} with Dr. {self.doctor} on {self.date} at {self.time}"