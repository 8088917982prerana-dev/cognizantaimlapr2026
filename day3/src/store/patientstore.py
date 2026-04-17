class patientstore:
    def __init__(self):
        self.patients = []
    def add_patient(self, patient):
        self.patients.append(patient)
    def get_all_patients(self):
        return self.patients
    def get_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(f"Patient with ID {patient_id} not found")
    def update_patient(self, patient_id, name=None, age=None):
        patient = self.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
    def delete_patient(self, patient_id):
        self.patients = [patient for patient in self.patients if patient.id != patient_id]