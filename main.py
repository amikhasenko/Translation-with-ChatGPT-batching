from _1_split_epub import *
from _2_create_request import *
from _3_create_batch import *
from _4_retrieve_batch import *
from _5_batch_to_txt import *
from _6_merge import *

import tomllib  # For Python 3.11+
# import toml   # Uncomment this for Python 3.10 or earlier

# Load the constants from the `.toml` file
with open("config.toml", "rb") as f:
    config = tomllib.load(f)
    constants = config["constants"]

# Unpack the dictionary into local variables
locals().update(constants)

def send_batch():
    split_epub(epub_path, txt_requests_folder, max_chars)
    create_request_jsonl(txt_requests_folder, requests_file, prompt)

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

def finish():
    client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
    with open("batch.json", "r") as file:
        batch_data = json.load(file)
    results_ready = retreve(client, batch_data["batch_id"])
    if (not results_ready) or \
        (input("Are you ready to replace epub with translation (y/n): ") != "y"): 
            return
    to_txt(result_file, translation_folder)
    merge(translation_folder, html_directory)
    html_files = [f for f in os.listdir(html_directory) if f.endswith('.html')]
    update_epub(epub_path, html_files)

if __name__=="__main__":
    stage = int(input("What stage are you in?\n (1) Configured .toml file and tocken, ready to go!\n (2) Want to check if results are ready \n Your stage: "))
    if stage == 1:
        send_batch()
    elif stage == 2:
        finish()
    else:
        print("Enter 1 or 2")