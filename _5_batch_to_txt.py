import json
import os

# Define the input file and output file pattern


def to_txt(input_file, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Parse the JSON line
            data = json.loads(line)
            
            # Extract the request number from custom_id
            custom_id = data['custom_id']
            request_number = custom_id.split('-')[1]  # This will give us the number i
            
            # Extract the content from the response
            content = data['response']['body']['choices'][0]['message']['content']
            
            # Define the output file name
            output_file = f'translation-{request_number}.txt'
            file_path = os.path.join(output_folder, output_file)
            # Write the content to the corresponding file
            with open(file_path, 'w') as output:
                output.write(content)

if __name__ == "__main__":
    input_file = 'output.jsonl'
    output_folder = 'translation'
    to_txt(input_file, output_folder)
