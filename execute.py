import ray
import time
import random
import sys
import json
import uuid
import os

# dummy data processor block
def data_processor(data):
    print(f"Starting data processor")
    
    # Simulate data processing time
    time.sleep(random.randint(10,20))
    
    # Perform data indexing
    print(f"Data processor ended")
    
    return data

# dummy data backup block
def data_backup(data):
    print(f"Starting data backup")
    file_uuid = uuid.uuid4()
    
    # Save to a file in temp_file directory
    with open(f"temp_files/{file_uuid}.txt", "w") as f:
        f.write(data)
    
    # Perform data indexing
    print(f"Data backup ended")
    
    return file_uuid

# Dummy test fetch data block
def test_fetch_data(file_uuid):
    print(f"Starting test fetch data")
    
    # Fetch data from file
    with open(f"temp_files/{file_uuid}.txt", "r") as f:
        data = f.read()
    
    # print current running path to debug the file location
    print(f"Current running path: {os.getcwd()}")
    
    # Perform data indexing
    print(f"Test fetch data ended")
    
    return data

# Data indexer block
@ray.remote
def data_indexer(data):
    print(f"Starting data indexer")
    
    # call data processor
    data = data_processor(data)
    # call data backup
    file_uuid = data_backup(data)
    # call test fetch data
    test_data = test_fetch_data(file_uuid)

    # if data == test_data: then update the ray job status to success, if not then update to failed
    if data == test_data:
        print(f"Data indexer ended")
        return data
    else:
        print(f"Data indexer failed")
        return None

if __name__ == "__main__":
    ray.init()

    input_data = json.loads(sys.argv[1])
    data = input_data["data"]

    result = ray.get(data_indexer.remote(data))
    print(json.dumps({"result": result}))
