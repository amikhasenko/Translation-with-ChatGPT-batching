import json
import os

# Define the range of request files and the directory
request_range = range(35)  # From request-0 to request-34
input_directory = 'output_requests'  # Directory containing the request files
output_file = 'requests.jsonl'  # Output JSONL file

# Open the output file for writing
with open(output_file, 'w', encoding='utf-8') as jsonl_file:
    for i in request_range:
        # Define the filename with the directory
        filename = os.path.join(input_directory, f'request-{i}.txt')
        
        # Check if the file exists
        if os.path.exists(filename):
            # Read the content of the file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                
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
                            "content": (
                                "Please translate the following text from English to German while maintaining "
                                "the markdown of the html document, tone, style, and specific terminology that "
                                "are characteristic of the Re: zero light novel series. Focus on preserving "
                                "the emotional nuances of each character's dialogue and the detailed descriptions "
                                "that contribute to the fantasy setting. Aim for a translation that reflects both "
                                "the formal and casual language used in the series. Don't translate <!-- Source: "
                                "{filename} -->. Don't add additional comments besides translation"
                            )
                        },
                        {
                            "role": "user",
                            "content": "```\n"+content+"\n```"
                        }
                    ]
                }
            }
            
            # Write the request structure to the JSONL file
            jsonl_file.write(json.dumps(request_structure) + '\n')
        else:
            print(f"File {filename} does not exist.")

print(f"Requests have been written to {output_file}.")
