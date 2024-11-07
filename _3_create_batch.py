import os
from openai import OpenAI
import json

def upload_file(client, file):
    """
    Uploads a file to the client's server for batch processing and returns the file ID.
    
    Parameters:
    ----------
    client : openai.OpenAI
        The API client instance used to communicate with the server.
    file : str
        Path to the file to upload.

    Returns:
    -------
    str
        The ID of the uploaded file.
    """
    batch_input_file = client.files.create(
        file=open(file, "rb"),
        purpose="batch"
    )
    batch_input_file_id = batch_input_file.id
    return batch_input_file_id

def create_batch(client, batch_input_file_id):
    """
    Creates a batch processing job for the uploaded file, with a 24-hour completion window, 
    and returns the batch ID.
    
    Parameters:
    ----------
    client : openai.OpenAI
        The API client instance used to communicate with the server.
    batch_input_file_id : str
        The ID of the uploaded file for processing.

    Returns:
    -------
    str
        The ID of the created batch job.
    """
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