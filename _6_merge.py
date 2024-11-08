import os
import re
import zipfile
import os

def merge(input_directory, output_directory):
    """
    Merges multiple translation text files into corresponding HTML files in the output directory.
    
    This function reads translation text files, extracts the translated content, and appends it to the appropriate
    target HTML files in the output directory based on the provided file names in the translation files.

    Parameters:
    ----------
    input_directory : str
        Path to the directory containing the translation text files.
    output_directory : str
        Path to the directory where the HTML files will be written or appended with translated content.

    Returns:
    -------
    None
        The function does not return anything but writes content into the specified output directory.
    """
    os.makedirs(output_directory, exist_ok=True)
    # Loop through all files named translation-0.txt to translation-n.txt
    file_pattern = re.compile(r'translation-(\d+)\.txt')
    request_files = [f for f in os.listdir(input_directory) if file_pattern.match(f)]
    request_indices = sorted(int(file_pattern.match(f).group(1)) for f in request_files)
    missing = set(range(max(request_indices)+1)) - set(request_indices)
    if len(missing) != 0:
        if input("Following indexes missing: "+", ".join([str(s) for s in missing])+". Continue? (y/n) ") != "y":
            return
    for i in request_indices:
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


def update_epub(epub_path, html_files):
    """
    Updates an existing EPUB file by adding or replacing HTML files.

    This function opens the specified EPUB file, and adds or replaces HTML files provided in the `html_files` list.
    It appends new content or replaces existing files inside the EPUB archive.

    Parameters:
    ----------
    epub_path : str
        Path to the existing EPUB file to be updated.
    html_files : list[str]
        List of paths to the HTML files that need to be added or updated in the EPUB.

    Returns:
    -------
    None
        The function does not return anything but modifies the EPUB file by adding or updating HTML files.
    """
    # Check if the EPUB file already exists
    if os.path.exists(epub_path):
        # Open the existing EPUB as a ZIP archive
        with zipfile.ZipFile(epub_path, 'a') as epub_zip:
            for html_file in html_files:
                file_name = os.path.basename(html_file)
                with open(html_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Check if the file already exists in the EPUB
                if file_name in epub_zip.namelist():
                    print(f"Replacing {file_name} in {epub_path}")
                else:
                    print(f"Adding {file_name} to {epub_path}")
                
                # Add or replace the HTML file in the EPUB
                epub_zip.writestr(file_name, html_content)


if __name__=="__main__":
    # Define the input and output directories
    epub_path = "[WN] ReZero - Volume 37.epub"
    input_directory = 'translation'
    output_directory = 'html'
    # merge(input_directory, output_directory, epub_path)
    html_files = [os.path.join(output_directory, f) for f in os.listdir(output_directory) if f.endswith('.html')]
    update_epub(epub_path, html_files)