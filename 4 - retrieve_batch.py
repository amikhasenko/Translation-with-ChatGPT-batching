import os
from openai import OpenAI
client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

files = client.files.list()
'''
It's posible to list all batches:
curl https://api.openai.com/v1/batches?limit=2 \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json"
or client.batches.list(limit=10)

You can also list all files:
curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer $OPENAI_API_KEY"
or client.files.list(limit=10)
'''
print(files.data)

file_response = client.files.content(files[0].id)
with open("batch_translations.jsonl") as f:
    f.write(file_response)