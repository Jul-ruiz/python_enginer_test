import os
import csv
import logging
import pandas as pd
import os
import pydicom


def list_folder_contents(path):
    try:
        elements = os.listdir(path)
        print(f"Number of elements inside '{path}': {len(elements)}")
        for element in elements:
            print(element)
    except Exception as e:
        logging.error(f"Error listing folder contents: {e}")


logging.basicConfig(level=logging.ERROR)

def read_csv_file(path, filename):
    try:
        full_path = os.path.normpath(os.path.join(path, filename))

        print("this is the path :",full_path)
        if not filename.endswith('.csv'):
            raise ValueError("The file is not a CSV file.")
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"{filename} does not exist.")
        
        df = pd.read_csv(full_path, delimiter=',',encoding='utf-8')
        print(f"Number of columns: {len(df.columns)}")
        print("Column names:", list(df.columns))
        print(f"Number of rows: {len(df)}")

        for column in df.select_dtypes(include=['number']).columns:
            print(f"Column '{column}':")
            print(f"  Average: {df[column].mean()}")
            print(f"  Standard Deviation: {df[column].std()}")

    except Exception as e:
        logging.error(e)



logging.basicConfig(level=logging.ERROR)

def read_dicom_file(path, filename, *tags):
    try:
        full_path = os.path.join(path,filename)
        if not filename.endswith('.dcm'):
            raise ValueError("The file is not a DICOM file.")
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"{filename} does not exist.")

        dicom_data = pydicom.dcmread(full_path)
        print(f"Patient's Name: {dicom_data.PatientName}")
        print(f"Study Date: {dicom_data.StudyDate}")
        print(f"Modality: {dicom_data.Modality}")

        for tag in tags:
            try:
                element = dicom_data[tag]
                print(f"Tag {tag}: {element.value}")
            except KeyError:
                print(f"Tag {tag} not found in the DICOM file.")

    except Exception as e:
        logging.error(e)


list_folder_contents(r"C:\Users\1\Documents\anyoneai\Test_python\prueba_python\env")

read_csv_file(r"C:\Users\1\Documents\anyoneai\Test_python\prueba_python", "sample-01-csv.csv")

read_dicom_file(r"C:\Users\1\Documents\anyoneai\Test_python\prueba_python", "sample-02-dicom.dcm","0x0008","0x0008")