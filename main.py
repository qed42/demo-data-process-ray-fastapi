from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from ray.job_submission import JobSubmissionClient
import json

app = FastAPI()
ray_client = JobSubmissionClient("http://127.0.0.1:8265")

class IndexAllRequest(BaseModel):
    data_uri: list[str]

class StatusRequest(BaseModel):
    job_id: str

@app.post("/index-all")
async def handle_index_all(request: IndexAllRequest, background_tasks: BackgroundTasks):
    job_ids = []
    for data_uri in request.data_uri:
        job_id = ray_client.submit_job(
            entrypoint="python execute.py '" + json.dumps({"data": data_uri}) + "'",
            runtime_env={"working_dir": "."}
        )
        job_ids.append(job_id)
    return {"job_ids": job_ids}

@app.post("/status")
async def handle_status(request: StatusRequest):
    return ray_client.get_job_status(request.job_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)