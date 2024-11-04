import json
import os
import re

def create_request_jsonl(input_directory, output_file, prompt):

    # List all filenames in the input directory that match the pattern 'request-<number>.txt'
    file_pattern = re.compile(r'request-(\d+)\.txt')
    request_files = [f for f in os.listdir(input_directory) if file_pattern.match(f)]

    # Extract the indices from the filenames and sort them
    request_indices = sorted(int(file_pattern.match(f).group(1)) for f in request_files)
    missing = set(range(max(request_indices)+1)) - set(request_indices)
    if len(missing) != 0:
        if input("Following indexes missing: "+", ".join([str(s) for s in missing])+". Continue? (y/n) ") != "y":
            return

    # Open the output file for writing
    with open(output_file, 'w', encoding='utf-8') as jsonl_file:
        for i in request_indices:
            # Define the filename with the directory
            filename = os.path.join(input_directory, f'request-{i}.txt')
            
            # Check if the file exists (redundant here but ensures safety)
            if os.path.exists(filename):
                # Read the content of the file
                with open(filename, 'r', encoding='utf-8') as file:
                    content = "```\n" + file.read() + "\n```"
                    
                # Create the request structure
                request_structure = {
                    "custom_id": f"request-{i}",
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": "gpt-4o-mini",
                        "messages": [
                            {
                                "role": "system",
                                "content": prompt,
                            },
                            {
                                "role": "user",
                                "content": content,
                            }
                        ]
                    }
                }
                
                # Write the request structure to the JSONL file
                jsonl_file.write(json.dumps(request_structure) + '\n')
            else:
                print(f"File {filename} does not exist.")  # Should not occur due to the filtering logic

    print(f"Requests have been written to {output_file}.")


if __name__=="__main__":
    # Define the input directory and output file
    input_directory = 'output_requests'  # Directory containing the request files
    output_file = 'requests.jsonl'  # Output JSONL file
    prompt = (
        "Please translate the following text from English to German while maintaining "
        "the markdown of the html document, tone, style, and specific terminology that "
        "are characteristic of the Re: zero light novel series. Focus on preserving "
        "the emotional nuances of each character's dialogue and the detailed descriptions "
        "that contribute to the fantasy setting. Aim for a translation that reflects both "
        "the formal and casual language used in the series. Don't translate <!-- Source: "
        "{filename} -->. Don't add additional comments besides translation"
    )
    create_request_jsonl(input_directory, output_file, prompt)