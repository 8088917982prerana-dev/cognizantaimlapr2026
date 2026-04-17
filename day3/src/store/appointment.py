"""create appointment crud operation"""
import sys
import os
from exceptions.appointment_not_found import AppointmentNotFound

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)
from conf.logger_conf import setup_logger
logger = setup_logger()

class appointmentstore:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        logger.info(f"Adding appointment: {appointment}")
        self.appointments.append(appointment)

    def get_all_appointments(self):
        logger.info("Fetching all appointments")
        return self.appointments

    def get_appointment_by_id(self, appointment_id):
        logger.info(f"Fetching appointment by ID: {appointment_id}")
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        raise AppointmentNotFound(f"Appointment with ID {appointment_id} not found")

    def update_appointment(self, appointment_id, doctor=None, patient=None, date=None):
        logger.info(f"Updating appointment: {appointment_id}")
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            if doctor:
                appointment.doctor = doctor
            if patient:
                appointment.patient = patient
            if date:
                appointment.date = date

    def delete_appointment(self, appointment_id):
        logger.info(f"Deleting appointment: {appointment_id}")
        self.appointments = [appointment for appointment in self.appointments if appointment.appointment_id != appointment_id]