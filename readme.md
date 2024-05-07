# DEMO: Data Indexing and Processing with Ray and FastAPI

This project demonstrates a extremly simple data indexing and processing system using Ray for distributed computing and FastAPI for creating a REST API.

## Prerequisites

- Python 3.11

## Installation

1. Clone the repository:
```
git clone https://github.com/qed42/demo-data-process-ray-fastapi.git
cd demo-data-process-ray-fastapi
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

3. Install the required packages:
```
pip install fastapi uvicorn ray
```

## Code Explanation

The project consists of two main files:

- `main.py`: Contains the FastAPI application and API endpoints.
- `execute.py`: Contains the Ray remote functions for data processing, backup, and indexing.

The `main.py` file defines two API endpoints:

- `/index-all` (POST): Accepts a list of data URIs and submits Ray jobs for each URI to process and index the data.
- `/status` (POST): Accepts a job ID and returns the status of the corresponding Ray job.

The `execute.py` file defines the following Ray remote functions:

- `data_processor`: Simulates data processing by sleeping for a random duration.
- `data_backup`: Saves the processed data to a temporary file.
- `test_fetch_data`: Retrieves the saved data from the temporary file for testing purposes.
- `data_indexer`: Orchestrates the data processing, backup, and testing steps.

## Running the Project

1. Start the Ray dashboard:
```
ray start --head
```
This will start the Ray dashboard at `http://127.0.0.1:8265`.

2. In a separate terminal, navigate to the project directory and start the FastAPI application:
```
uvicorn main:app --reload
```
This will start the FastAPI application at `http://127.0.0.1:8000`.

## Using the API Endpoints

1. To submit data for indexing, send a POST request to the `/index-all` endpoint with a JSON payload containing a list of data URIs:
```
curl -X POST -H "Content-Type: application/json" -d '{"data_uri": ["data1", "data2", "data3"]}' http://localhost:8000/index-all
```
This will return a response containing the job IDs for each submitted data URI.

2. To check the status of a job, send a POST request to the `/status` endpoint with a JSON payload containing the job ID:
```
curl -X POST -H "Content-Type: application/json" -d '{"job_id": "raysubmit_your-job-id"}' http://localhost:8000/status
```
This will return the status of the specified job.

## Important Note

The temporary files generated during data backup are saved in a Ray temporary directory, not in the current directory. The path of the temporary directory will be similar to:
```
/tmp/ray/session_2024-05-07_05-59-13_029854_252170/runtime_resources/working_dir_files/_ray_pkg_dd57f4b2a82d80a9
```
Please keep this in mind when accessing or cleaning up the temporary files.
