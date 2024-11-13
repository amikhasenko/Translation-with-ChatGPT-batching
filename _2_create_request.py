import json
import os
import re

def create_request_jsonl(input_directory, output_file, prompt):
    """
    Creates a JSON Lines (JSONL) file containing structured API requests based on text files in an input directory.

    This function reads text files with names matching the pattern `request-<number>.txt` from a specified input
    directory. It then formats the content of each file as a "user" message in a JSON request structure, adding a
    "system" message with the specified prompt. Each structured request is written as a JSON object to a JSONL file,
    with one request per line.

    Parameters:
    ----------
    input_directory : str
        Path to the directory containing the text files (`request-<number>.txt`) to process.
    output_file : str
        Path to the JSONL file where the formatted requests will be saved.
    prompt : str
        The prompt text for the "system" message in each request, providing context or instructions.

    Process:
    -------
    1. Finds files in `input_directory` matching the naming pattern `request-<number>.txt`.
    2. Sorts files by numeric order to maintain sequence in the output.
    3. Detects missing indices in the sequence and prompts the user to continue if any are missing.
    4. For each file, constructs a JSON object for an API request with:
       - `custom_id`: unique identifier for each request, based on the file name.
       - `method`: "POST", indicating an API request method.
       - `url`: API endpoint path.
       - `body`: JSON object with "model" specification, system message (`prompt`), and user message (`content`).
    5. Writes each JSON object to the JSONL file, one per line.

    Returns:
    -------
    None
        The function writes the formatted requests to the specified JSONL file but does not return any value.

    Example:
    -------
    >>> create_request_jsonl("input_directory", "output_requests.jsonl", "Translate the following text.")
    # This will produce a JSONL file named `output_requests.jsonl`, with each line representing an API request.

    Notes:
    ------
    - The function prompts the user if any `request-<number>.txt` files are missing from the sequence, allowing
      the user to continue or stop.
    - The "content" of each request is wrapped in triple backticks (```) to format it as a code block.

    Dependencies:
    ------------
    Requires `os`, `re`, and `json` modules for file handling, pattern matching, and JSON serialization.
    """

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
                        ],
                        "temperature": 0.4,
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