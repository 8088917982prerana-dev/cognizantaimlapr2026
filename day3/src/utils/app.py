import sys
import os
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'..', '..')
)
src_path = os.path.join(project_root, 'src')
sys.path.append(src_path)
sys.path.append(project_root)
from model.patient import patient
from model.doctor import doctor
from model.appointment import appointment

from conf.logger_conf import setup_logger
"""
entry for healthcare application
"""
logger = setup_logger()
def run():
    """
    test logger
    """
    from datetime import datetime
    doctor1 = doctor(1, "Dr. Smith", "Cardiology")
    doctor2 = doctor(2, "Dr. Johnson", "Neurology")
    patient1 = patient("Alice", 1, "1994-01-15", "Hypertension")
    patient2 = patient("Bob", 2, "1999-05-20", "Diabetes")
    appointment1 = appointment(1, patient1, doctor1, datetime(2024, 6, 1, 10, 0), "10:00 AM")
    appointment2 = appointment(2, patient2, doctor2, datetime(2024, 6, 2, 11, 0), "11:00 AM")
    logger.info(f"Created doctor: {doctor1}")
    logger.info(f"Created doctor: {doctor2}")
    logger.info(f"Created patient: {patient1}")
    logger.info(f"Created patient: {patient2}")
    logger.info(f"Created appointment: {appointment1}")
    logger.info(f"Created appointment: {appointment2}")
    logger.info("app run")
    """
handle entry point
"""
if __name__ == "__main__":
    run()
