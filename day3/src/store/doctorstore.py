"""create doctor crud operation"""
import sys
import os
from model.doctor import doctor
from exceptions.doctor_not_found_exception import doctornotfoundexception

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from conf.logger_conf import setup_logger
logger = setup_logger()

class DoctorStore:
    def __init__(self):
        self.doctors = []
    
    def add_doctor(self, doctor: doctor):
        logger.info(f"Adding doctor: {doctor}")
        self.doctors.append(doctor)

    def get_all_doctors(self):
        logger.info("Fetching all doctors")
        return self.doctors
    
    def get_doctor_by_id(self, doctor_id: int):
        logger.info(f"Fetching doctor with ID: {doctor_id}")
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        raise doctornotfoundexception(f"Doctor with ID {doctor_id} not found")
        
    
    def update_doctor(self, doctor_id: int, name: str = None, specialty: str = None):
        doctor = self.get_doctor_by_id(doctor_id)
        logger.info(f"Updating doctor with ID: {doctor_id}")
        if doctor:
            if name:
                doctor.name = name
            if specialty:
                doctor.specialty = specialty
    
    def delete_doctor(self, doctor_id: int):
        logger.info(f"Deleting doctor with ID: {doctor_id}")
        self.doctors = [doctor for doctor in self.doctors if doctor.id != doctor_id]