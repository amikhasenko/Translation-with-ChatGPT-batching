import os
from openai import OpenAI
import json

def upload_file(client, file):
    batch_input_file = client.files.create(
        file=open(file, "rb"),
        purpose="batch"
    )
    batch_input_file_id = batch_input_file.id
    return batch_input_file_id

def create_batch(client, batch_input_file_id):
    batch = client.batches.create(
        input_file_id=batch_input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
        metadata={
            "description": "Translation"
        }
    )
    return batch.id

if __name__ == "__main__":
    client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
    request_file_id = upload_file(client, "requests.jsonl")
    batch_id = create_batch(client, request_file_id)
    with open("batch.json", "w") as file:
        json.dump(
            {
                "request_file_id": request_file_id, 
                "batch_id": batch_id,
            }, 
            file,
        )
    print("Batch uploaded, id dumped to batch.json")