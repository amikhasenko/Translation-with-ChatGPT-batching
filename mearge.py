import os

# Loop through all files named request-0.txt to request-34.txt
for i in range(35):
    filename = f'request-{i}.txt'
    
    # Open and read the current file
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Extract the filename from the first line and content to be written
    target_filename = lines[0].strip().split(': ')[1].replace('-->', '').strip()
    content = ''.join(lines[1:])  # Join lines excluding the first one
    
    # Write or append to the target file
    write_mode = 'a' if os.path.exists(target_filename) else 'w'
    with open(target_filename, write_mode) as target_file:
        if write_mode == 'a':  # Append mode, add newline first
            target_file.write('\n')
        target_file.write(content)
