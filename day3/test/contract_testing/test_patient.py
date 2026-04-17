"""
test for patient contract
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

from model.patient import patient

"""
test for patient object creation
"""
@pytest.fixture
def initialize_patient():
    """
    initialize patient object
    """
    # Matches (name, id, dob, ailment) per your patient.py structure
    pat = patient("John Doe", 101, "1990-05-15", "Flu")
    return pat

def read_patient_data_from_csv(file_path):
    """
    read patient data from csv file
    """
    patient_data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Matches the CSV columns: id, name, dob, ailment
            patient_data.append((
                int(row['id']), 
                row['name'], 
                row['dob'], 
                row['ailment']
            ))
    return patient_data

def test_patient_creation(initialize_patient):
    """
    test patient object creation
    """
    assert initialize_patient.name == "John Doe"
    assert initialize_patient.id == 101
    assert initialize_patient.dob == "1990-05-15"
    assert initialize_patient.ailment == "Flu"

@pytest.mark.parametrize("id, name, dob, ailment", read_patient_data_from_csv('test/patients.csv'))
def test_patient_creation_parametrize(id, name, dob, ailment):
    """
    test patient object creation with parametrize
    """
    # Important: passing arguments in the order expected by patient.__init__
    pat = patient(name, id, dob, ailment)
    
    assert pat.id == id
    assert pat.name == name
    assert pat.dob == dob
    assert pat.ailment == ailment