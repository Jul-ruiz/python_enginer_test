import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='patient_record.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class PatientRecord:
    def __init__(self, name, age, birth_date, sex, weight, patient_id, patient_id_type):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.sex = sex
        self.weight = weight
        self.patient_id = patient_id
        self.patient_id_type = patient_id_type
        self.diagnosis = None

    # Setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_sex(self, sex):
        self.sex = sex

    def set_weight(self, weight):
        self.weight = weight

    def set_patient_id(self, patient_id):
        self.patient_id = patient_id

    def set_patient_id_type(self, patient_id_type):
        self.patient_id_type = patient_id_type

    def set_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis

    # Getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_birth_date(self):
        return self.birth_date

    def get_sex(self):
        return self.sex

    def get_weight(self):
        return self.weight

    def get_patient_id(self):
        return self.patient_id

    def get_patient_id_type(self):
        return self.patient_id_type

    def get_diagnosis(self):
        return self.diagnosis

    # Method to update diagnosis and log the change
    def update_diagnosis(self, new_diagnosis):
        old_diagnosis = self.diagnosis
        self.diagnosis = new_diagnosis
        logging.info(f"Diagnosis updated for patient ID {self.patient_id}: '{old_diagnosis}' to '{new_diagnosis}'")
        print(f"Diagnosis updated for patient ID {self.patient_id}: '{old_diagnosis}' to '{new_diagnosis}'")

# Example usage
if __name__ == "__main__":
    # Create a patient record
    patient = PatientRecord(name="John Doe", age=30, birth_date="1994-05-12", sex="Male", 
                            weight=70.5, patient_id="12345", patient_id_type="SSN")

    # Update diagnosis
    patient.update_diagnosis("Hypertension")
    patient.update_diagnosis("Diabetes Type II")

