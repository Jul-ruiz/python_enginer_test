import logging
from datetime import datetime
import pydicom
from PatientRecord import PatientRecord 

class StudyRecord(PatientRecord):
    def __init__(self, name, age, birth_date, sex, weight, patient_id, patient_id_type):
        super().__init__(name, age, birth_date, sex, weight, patient_id, patient_id_type)
        self.modality = None
        self.study_date = None
        self.study_time = None
        self.study_instance_uid = None
        self.series_number = None
        self.number_of_frames = None

    # Setters
    def set_modality(self, modality):
        self.modality = modality

    def set_study_date(self, study_date):
        self.study_date = study_date

    def set_study_time(self, study_time):
        self.study_time = study_time

    def set_study_instance_uid(self, study_instance_uid):
        self.study_instance_uid = study_instance_uid

    def set_series_number(self, series_number):
        self.series_number = series_number

    def set_number_of_frames(self, number_of_frames):
        self.number_of_frames = number_of_frames

    # Getters
    def get_modality(self):
        return self.modality

    def get_study_date(self):
        return self.study_date

    def get_study_time(self):
        return self.study_time

    def get_study_instance_uid(self):
        return self.study_instance_uid

    def get_series_number(self):
        return self.series_number

    def get_number_of_frames(self):
        return self.number_of_frames

    # Load study details from a DICOM file
    def load_from_dicom(self, dicom_file_path):
        try:
            dicom_data = pydicom.dcmread(dicom_file_path)

            self.modality = dicom_data.Modality if 'Modality' in dicom_data else None
            self.study_date = dicom_data.StudyDate if 'StudyDate' in dicom_data else None
            self.study_time = dicom_data.StudyTime if 'StudyTime' in dicom_data else None
            self.study_instance_uid = dicom_data.StudyInstanceUID if 'StudyInstanceUID' in dicom_data else None
            self.series_number = dicom_data.SeriesNumber if 'SeriesNumber' in dicom_data else None
            self.number_of_frames = dicom_data.NumberOfFrames if 'NumberOfFrames' in dicom_data else None

            logging.info(f"Study details loaded from DICOM file: {dicom_file_path}")

        except Exception as e:
            logging.error(f"Failed to load DICOM file: {dicom_file_path}. Error: {e}")

        # Overriding the __str__ method to print patient and study information

    def __str__(self):
        return (f"Patient Information:\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Birth Date: {self.birth_date}\n"
                f"Sex: {self.sex}\n"
                f"Weight: {self.weight} kg\n"
                f"Patient ID: {self.patient_id}\n"
                f"Patient ID Type: {self.patient_id_type}\n"
                f"\nStudy Information:\n"
                f"Modality: {self.modality}\n"
                f"Study Date: {self.study_date}\n"
                f"Study Time: {self.study_time}\n"
                f"Study Instance UID: {self.study_instance_uid}\n"
                f"Series Number: {self.series_number}\n"
                f"Number of Frames: {self.number_of_frames}\n")


