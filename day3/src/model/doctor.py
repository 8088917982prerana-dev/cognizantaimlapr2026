"""
defines the doctor class
"""
class doctor:
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Doctor {self.id}: {self.name}, Specialty: {self.specialty}"