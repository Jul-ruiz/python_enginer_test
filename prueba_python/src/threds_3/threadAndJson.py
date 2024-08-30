import threading
import json
import os
import logging
from concurrent.futures import ThreadPoolExecutor

# Logging configuration
logging.basicConfig(filename='shared_log.log', level=logging.INFO, 
                    format='%(asctime)s:%(threadName)s:%(message)s')

# Function to normalize data and log information
def process_element(element):
    element_id = element['id']
    data = [int(num) for line in element['data'] for num in line.split()]
    max_value = max(data)
    normalized_data = [x / max_value for x in data]
    
    avg_before = sum(data) / len(data)
    avg_after = sum(normalized_data) / len(normalized_data)
    data_size = len(data)
    
    # Log information
    logging.info(f"Element ID: {element_id}")
    logging.info(f"Average before normalization: {avg_before}")
    logging.info(f"Average after normalization: {avg_after}")
    logging.info(f"Data size: {data_size}")
    
    # Print information
    print(f"Element ID: {element_id}")
    print(f"Average before normalization: {avg_before}")
    print(f"Average after normalization: {avg_after}")
    print(f"Data size: {data_size}")

# Function to load the JSON and process it using threads
def process_json_file(json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        for key in json_data:
            executor.submit(process_element, json_data[key])

# Main function with predefined values
def main():
    folder_path = r"C:\Users\1\Documents\anyoneai\Test_python\prueba_python"
    json_filename = "sample-03-00-json.json"
    json_file_path = os.path.join(folder_path, json_filename)
    # json_file_path = os.path.normpath(os.path.join(folder_path, json_filename))
    
    if not os.path.exists(json_file_path):
        print(f"File {json_file_path} does not exist.")
        return
    
    process_json_file(json_file_path)

if __name__ == "__main__":
    main()


