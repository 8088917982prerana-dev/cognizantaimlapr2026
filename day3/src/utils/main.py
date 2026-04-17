import sys
import os
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'..', '..')
)
src_path = os.path.join(project_root, 'src')
sys.path.append(project_root)
sys.path.append(src_path)
from conf.logger_conf import setup_logger
logger = setup_logger()
def create_person():
    """
    create person object
    """
    from model.person import person
    person1 = person(123456789012, 9876543210)
    print(f"Created person: Aadhar - {person1.aadhar_number}, Mobile - {person1.mobile_no}")
    """
    update mobile number
    """
    try:
        person1.mobile_no = 12345  # Invalid mobile number
        logger.info(f"Updated mobile number: {person1.mobile_no}")
    except ValueError as e:
        logger.error(f"Error: {e}")
def create_staff():
    """
    create staff object
    """
    from model.staff import staff
    role=role(name="Nurse", description="treats children")
    staff1 = staff(123456678901, 9876543210, role)
    print(f"Created staff: Aadhar - {staff1.aadhar_number}, Mobile - {staff1.mobile_no}, Role - {staff1.role}")
if __name__ == "__main__":
    create_person()
    create_staff()