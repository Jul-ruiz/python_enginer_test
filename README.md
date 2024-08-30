## Project Title: Python Developer I Test - Medical Image Processing System

# Overview

This project was completed as part of a Python Developer I technical test. It involves a comprehensive set of tasks that test skills in file handling, data processing, object-oriented programming, multithreading, RESTful API design, and the design of a distributed system. The project focuses on processing medical images, particularly DICOM files, and managing the results through a scalable, fault-tolerant system.

## The project is organized into different directories, each corresponding to a specific task:

# API Implementation: The RESTful API is located in the django_api_proyect directory. This is where the Django-based API for managing medical image processing results is developed.

# Other Tasks: Located in the src directory, with the following subdirectories:

# rrays_1: File Handling and Array Operations.
# oop_app_2: Object-Oriented Programming (OOP).
# threds_3: Multithreading and Concurrency.
# z_architecture_5: Distributed DICOM Processing System Design.

## 1. File Handling and Array Operations (src/arrays_1)

Task Description:

List folder contents: A function to count and print the number of elements inside a given folder path.

Read CSV file: A function to read a CSV file, print the column names, row count, and calculate the average and standard deviation for numeric columns. Error handling and logging are included for non-existent files, non-CSV files, and non-numeric data.

Read DICOM file: A function to read a DICOM file using pydicom, printing the patient's name, study date, and modality. Optionally, it can print additional DICOM tags.
Key Features:

Robust error handling and logging.
Detailed output for data analysis from CSV and DICOM files.

## 2. Object-Oriented Programming (OOP) (src/oop_app_2)

Task Description:

PatientRecord Class: Stores patient information such as name, age, birth date, sex, weight, and patient ID. Includes methods to set and get this information, as well as a method to update and log diagnosis changes.

StudyRecord Class: Inherits from PatientRecord and stores study-related information like modality, study date, and study time. It also includes a method to load all study details from a DICOM file and overrides the __str__ method to print comprehensive information about the patient and study.

Key Features:

OOP principles applied to medical record management.

Integration with DICOM files for automated study data extraction.

## 3. Multithreading and Concurrency (src/threds_3)

Task Description:

Even and Odd Numbers: A script that spawns two threads—one to print even numbers and another to print odd numbers between 1 and 200 with a 0.5-second interval.

JSON File Processing: A program that reads a JSON file and processes each element using threads, with a limit of 4 concurrent threads. Each thread normalizes data, computes averages before and after normalization, and logs the results safely to a shared log file.

Key Features:

Efficient multithreading with controlled concurrency.

Thread-safe logging for data processing.

## 4. RESTful API Design (django_api_proyect)

Task Description:
Django RESTful API: A Django-based API for CRUD operations to manage medical image processing results stored in a PostgreSQL database. The API includes endpoints for creating, reading, updating, and deleting entries, with robust data validation and logging of all activities.

Key Features:

Full CRUD functionality with a PostgreSQL backend.
API request and response logging for monitoring and debugging.

## 5. Distributed DICOM Processing System (Design and Architecture) (src/z_architecture_5)

Task Description:

System Design: The task involves designing a distributed system for processing large batches of DICOM images across multiple machines. The system needs to ensure efficient task distribution, fault tolerance, scalability, and provide a user interface for result retrieval.

Key Features:

Scalable architecture with load balancing and resource management.
Secure and HIPAA/GDPR-compliant design considerations for medical data.

## Challenges Overcome

Throughout the development of this project, several challenges were addressed:

Data Integrity and Error Handling: Implementing robust error handling mechanisms, particularly when dealing with different file types (CSV, DICOM) and ensuring data integrity during processing and storage.

Concurrency Management: Managing multiple threads efficiently, ensuring thread safety while logging, and handling potential race conditions when processing JSON data concurrently.

API Design and Database Integration: Designing a RESTful API that adheres to best practices in API design, while ensuring that the database schema supports efficient CRUD operations for large datasets.

Scalability and Fault Tolerance: Designing a distributed system architecture that can scale to meet increasing demands while maintaining fault tolerance and ensuring the security of sensitive medical data.

## How to Run the Project

File Handling and OOP Tasks (src/arrays_1, src/oop_app_2):

Run the scripts directly using Python to process CSV, DICOM files, and manage patient and study records.
Multithreading Task (src/threds_3):

Execute the multithreading script to observe even and odd number printing, as well as JSON file processing with logging.
RESTful API (django_api_proyect):

Set up the Django project, configure PostgreSQL, and run the server. Use tools like Postman to interact with the API endpoints.
Distributed System Design (src/z_architecture_5):

Review the design document outlining the architecture and components needed for the distributed DICOM processing system.