import os
from openai import OpenAI
from datetime import datetime
import json

def retreve(client: OpenAI, batch_id: str):
    """
    Retrieves the status of a batch processing job and handles different statuses accordingly.
    
    Depending on the batch's status, it provides information about the job's progress or outcome, 
    including error handling and saving result files ("error.jsonl" and "output.jsonl") if available.

    Parameters:
    ----------
    client : openai.OpenAI
        The API client instance used to communicate with the server.
    batch_id : str
        The ID of the batch job to retrieve the status for.

    Returns:
    -------
    bool
        Returns `True` if the batch is completed successfully, `False` otherwise.
    """
    batch = client.batches.retrieve(batch_id)
    print(batch.status)
    if batch.status == "failed":
        print("Batch failed validation")
    elif batch.status in ["validating", "in_progress", "finalizing"]:
        print("Batch started at:", datetime.fromtimestamp(batch.created_at).strftime("%Y-%m-%d %H:%M:%S"))
        print("Batch is in progress, it tackes up to 24h")
    elif batch.status == "expired":
        print("Batch could not be completed within the SLA time window, probably servers overloaded")
    elif batch.status == "completed":
        print("Batch started at:", datetime.fromtimestamp(batch.created_at).strftime("%Y-%m-%d %H:%M:%S"))
        print("Batch completed at:", datetime.fromtimestamp(batch.completed_at).strftime("%Y-%m-%d %H:%M:%S"))
        print("Complited:",batch.request_counts.completed)
        print("Failed:",batch.request_counts.failed )
        if batch.error_file_id != None: 
            client.files.content(batch.error_file_id).write_to_file("error.jsonl")
        if batch.output_file_id != None: 
            client.files.content(batch.output_file_id).write_to_file("output.jsonl")
        return True
    else:
        print(batch.status)
    return False

if __name__ == "__main__":
    client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
    with open("batch.json", "r") as file:
        batch_data = json.load(file)
    retreve(client, batch_data["batch_id"])

