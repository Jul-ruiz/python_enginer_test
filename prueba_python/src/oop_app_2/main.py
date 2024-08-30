from StudyRecord import StudyRecord
from PatientRecord import PatientRecord


if __name__ == "__main__":

    patient = PatientRecord(name="camilo ", age=16, birth_date="1998-09-15", sex="Male",
                            weight=65.0, patient_id="67890", patient_id_type="MRN")
    # Create a study record
    study = StudyRecord(name="Jane Doe", age=28, birth_date="1996-02-15", sex="Female",
                        weight=65.0, patient_id="67890", patient_id_type="MRN")

    # Load study details from a DICOM file
    study.load_from_dicom(r"C:\Users\1\Documents\anyoneai\Test_python\prueba_python\sample-02-dicom.dcm")

    # Example of getting loaded data
    print("Modality:", study.get_modality())
    print("Study Date:", study.get_study_date())
    print("Study Time:", study.get_study_time())
    print("Study Instance UID:", study.get_study_instance_uid())
    print("Series Number:", study.get_series_number())
    print("Number of Frames:", study.get_number_of_frames())

    print("++++++++++++++++++")
    print(study)
    print(patient)
