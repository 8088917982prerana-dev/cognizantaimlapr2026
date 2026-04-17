"""
test for doctor contract
"""
import pytest
import sys
import os
import csv
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'..', '..')
)
src_path = os.path.join(project_root, 'src')
sys.path.append(src_path)
from model.doctor import doctor
"""
test for doctor object creation
"""
@pytest.fixture
def initialize_doctor():
    """
    initialize doctor object
    """
    doc = doctor(1, "Dr. Smith", "Cardiology")
    return doc
def read_doctor_data_from_csv(file_path):
    """
    read doctor data from csv file
    """
    doctor_data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            doctor_data.append((int(row['id']), row['name'], row['speciality']))
    return doctor_data
def test_doctor_creation(initialize_doctor):
    """
    test doctor object creation
    """
    assert initialize_doctor.id == 1
    assert initialize_doctor.name == "Dr. Smith"
    assert initialize_doctor.specialty == "Cardiology"
@pytest.mark.parametrize("id, name, specialty", read_doctor_data_from_csv('test/doctors.csv'))
def test_doctor_creation_parametrize(id, name, specialty):
    """
    test doctor object creation with parametrize
    """
    doc = doctor(id, name, specialty)
    assert doc.id == id
    assert doc.name == name
    assert doc.specialty == specialty
