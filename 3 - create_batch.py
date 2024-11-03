import os
from openai import OpenAI

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
batch_input_file = client.files.create(
  file=open("requests.jsonl", "rb"),
  purpose="batch"
)
batch_input_file_id = batch_input_file.id
print("file_id:", batch_input_file_id)

batch = client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
      "description": "Translation"
    }
)
print("batch_id:", batch.id)