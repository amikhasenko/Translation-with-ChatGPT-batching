import os

# Define the input and output directories
input_directory = 'translation'
output_directory = 'html'

# Loop through all files named translation-0.txt to translation-34.txt
for i in range(35):
    input_filename = os.path.join(input_directory, f'translation-{i}.txt')
    
    # Check if the input file exists before attempting to read it
    if os.path.exists(input_filename):
        # Open and read the current file
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        
        # Extract the filename from the first line and content to be written
        target_filename = lines[1].strip().split(': ')[1].replace('-->', '').strip()
        target_file_path = os.path.join(output_directory, target_filename)

        # Write or append to the target file
        write_mode = 'a' if os.path.exists(target_file_path) else 'w'
        with open(target_file_path, write_mode) as target_file:
            if write_mode == 'a':  # Append mode, add newline first
                target_file.write('\n')
            target_file.write(''.join(lines[2:-1]))  # Join lines excluding the first one
    else:
        print(f"File {input_filename} does not exist.")
