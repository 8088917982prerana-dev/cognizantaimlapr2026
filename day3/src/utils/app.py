import sys
import os
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'..', '..')
)
src_path = os.path.join(project_root, 'src')
sys.path.append(src_path)
from model.patient import patient
from model.doctor import doctor
from model.appointment import appointment
from store.doctorstore import DoctorStore
from store.patientstore import patientstore
from store.appointment import appointmentstore
from exceptions.appointment_not_found import AppointmentNotFound

from conf.logger_conf import setup_logger
"""
entry for healthcare application
"""
logger = setup_logger()

def doctor_run():
    """
    test logger
    """
    logger.info("=== doctor CRUD operations ===")
    doctor_store = DoctorStore()

    doctor1 = doctor(1, "Dr. Smith", "Cardiology")
    doctor2 = doctor(2, "Dr. Johnson", "Neurology")
    doctor3 = doctor(3, "Dr. Williams", "Pediatrics")

    doctor_store.add_doctor(doctor1)
    doctor_store.add_doctor(doctor2)
    doctor_store.add_doctor(doctor3)
    logger.info("Added 3 doctors")

    logger.info("Getting all doctors")
    doctors = doctor_store.get_all_doctors()
    logger.info(f"retrieved doctors: {doctors}")

    logger.info("Updating doctor")
    doctor_store.update_doctor(2, name="Dr. Johnson", specialty="Psychiatry")
    logger.info("Updated doctor 2")

    logger.info("Deleting doctor")
    deleted_doctor = doctor_store.delete_doctor(3)
    logger.info(f"Deleted doctor: {deleted_doctor}")

    logger.info("Testing error handling")
    try:
        doctor_store.get_doctor_by_id(999)
    except Exception as e:
        logger.error(f"Error occurred: {e}")

    return doctor_store

def patient_run():
    """patient crud operations"""
    logger.info("=== patient CRUD operations ===")
    patient_store = patientstore()
    from datetime import date

    logger.info("Adding patients")
    patient1 = patient("Alice", 1, "1994-01-15", "Hypertension")
    patient2 = patient("Bob", 2, "1999-05-20", "Diabetes")
    patient3 = patient("Charlie", 3, "2000-09-10", "Asthma")
    patient_store.add_patient(patient1)
    patient_store.add_patient(patient2)
    patient_store.add_patient(patient3)
    logger.info("Added 3 patients")

    logger.info("Getting all patients")
    patients = patient_store.get_all_patients()
    for patient_item in patients:
        logger.info(f"retrieved patient: {patient_item}")

    logger.info("Getting patient by id")
    patient_item = patient_store.get_patient_by_id(2)
    logger.info(f"retrieved patient: {patient_item}")

    logger.info("Updating patient")
    patient_store.update_patient(2, ailment="Diabetes, High Cholesterol")
    logger.info("Updated patient 2")

    logger.info("Deleting patient")
    deleted_patient = patient_store.delete_patient(3)
    logger.info(f"Deleted patient: {deleted_patient}")

    logger.info("Testing error handling")
    try:
        patient_store.get_patient_by_id(999)
    except Exception as e:
        logger.error(f"Error occurred: {e}")

    return patient_store

def appointment_run(doctor_store, patient_store):
    """
    appointment crud operations
    """
    logger.info("=== appointment CRUD operations ===")
    appointment_store = appointmentstore()
    from datetime import datetime

    doctors = doctor_store.get_all_doctors()
    patients = patient_store.get_all_patients()

    if len(doctors) < 2 or len(patients) < 2:
        logger.error("No doctors or patients available to create appointments")
        return appointment_store

    doctor1 = doctors[0]
    doctor2 = doctors[1]
    patient1 = patients[0]
    patient2 = patients[1]

    logger.info("Adding appointments")
    appointment1 = appointment(1, patient1, doctor1, datetime(2024, 6, 1, 10, 0), "10:00 AM")
    appointment2 = appointment(2, patient2, doctor2, datetime(2024, 6, 2, 11, 0), "11:00 AM")
    appointment3 = appointment(3, patient1, doctor2, datetime(2024, 6, 3, 9, 0), "9:00 AM")
    appointment_store.add_appointment(appointment1)
    appointment_store.add_appointment(appointment2)
    appointment_store.add_appointment(appointment3)
    logger.info("Added 3 appointments")

    logger.info("Getting all appointments")
    appointments = appointment_store.get_all_appointments()
    for appointment_item in appointments:
        logger.info(f"retrieved appointment: {appointment_item}")

    logger.info("Getting appointment by id")
    appointment_item = appointment_store.get_appointment_by_id(2)
    logger.info(f"retrieved appointment: {appointment_item}")

    logger.info("Updating appointment")
    appointment_store.update_appointment(2, doctor=doctor1, patient=patient2, date=datetime(2024, 6, 2, 11, 0))
    logger.info("Updated appointment 2")

    logger.info("Deleting appointment")
    deleted_appointment = appointment_store.delete_appointment(3)
    logger.info(f"Deleted appointment: {deleted_appointment}")

    logger.info("Testing error handling")
    try:
        appointment_store.get_appointment_by_id(999)
    except AppointmentNotFound as e:
        logger.error(f"Error occurred: {e}")

    return appointment_store

def run():
    """
    run all operations
    """
    logger.info("Starting healthcare application")
    doctor_store = doctor_run()
    patient_store = patient_run()
    appointment_store = appointment_run(doctor_store, patient_store)
    logger.info("Healthcare application finished")

"""
handle entry point
"""
if __name__ == "__main__":
    run()
