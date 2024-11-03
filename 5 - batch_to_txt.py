import json

# Define the input file and output file pattern
input_file = 'batch_67275398c1248190bda3ffd5bb68b469_output.jsonl'

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
        
        # Write the content to the corresponding file
        with open(output_file, 'w') as output:
            output.write(content)

print("Extraction complete!")
