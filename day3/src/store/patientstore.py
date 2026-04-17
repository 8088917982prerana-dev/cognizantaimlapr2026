"""create patient crud operation"""
import sys
import os
from model.patient import patient
from exceptions.patient_not_found_exception import patientnotfoundexception

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from conf.logger_conf import setup_logger
logger = setup_logger()

class patientstore:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: patient):
        logger.info(f"Adding patient: {patient}")
        self.patients.append(patient)

    def get_all_patients(self):
        logger.info("Fetching all patients")
        return self.patients

    def get_patient_by_id(self, patient_id):
        logger.info(f"Fetching patient by ID: {patient_id}")
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise patientnotfoundexception(f"Patient with ID {patient_id} not found")

    def update_patient(self, patient_id, name=None, dob=None, ailment=None):
        logger.info(f"Updating patient: {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if dob:
                patient.dob = dob
            if ailment:
                patient.ailment = ailment

    def delete_patient(self, patient_id):
        logger.info(f"Deleting patient: {patient_id}")
        self.patients = [patient for patient in self.patients if patient.id != patient_id]