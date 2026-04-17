"""create doctor crud operation"""
import pytest
import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
src_path = os.path.join(project_root, 'src')
sys.path.append(src_path)

from model.doctor import doctor
from exceptions.doctor_not_found_exception import doctornotfoundexception
from store.doctorstore import DoctorStore
def test_doctor_not_found_exception():
    """
    test doctor not found exception
    """
    doctor_store = DoctorStore()
    with pytest.raises(doctornotfoundexception):
        doctor_store.get_doctor_by_id(999)  # Assuming 999 is an ID that doesn't exist
