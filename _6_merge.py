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


def create_epub_copy(original_epub_path, html_files):
    """
    Creates a copy of an existing EPUB file with specified HTML files added or replaced.

    Parameters:
    ----------
    original_epub_path : str
        Path to the original EPUB file to be copied and updated.
    html_files : list[str]
        List of paths to the HTML files that need to be added or updated in the new EPUB.

    Returns:
    -------
    None
        The function creates a new EPUB file with updated HTML files.
    """
    # Set to store the names of new or updated files
    new_epub_path = original_epub_path[:-5]+"-ChatGPT-translated.epub"
    html_filenames = {os.path.basename(html_file) for html_file in html_files}

    # Open the original EPUB as a ZIP archive in read mode
    with zipfile.ZipFile(original_epub_path, 'r') as original_epub:
        # Create a new EPUB file (copy) in write mode
        with zipfile.ZipFile(new_epub_path, 'w') as new_epub:
            # Copy all files from the original EPUB to the new EPUB
            for item in original_epub.infolist():
                # If the file is not in `html_files`, copy it directly
                if item.filename not in html_filenames:
                    new_epub.writestr(item, original_epub.read(item.filename))
            
            # Add or replace HTML files specified in `html_files`
            for html_file in html_files:
                file_name = os.path.basename(html_file)
                with open(html_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                print(f"{'Replacing' if file_name in original_epub.namelist() else 'Adding'} {file_name} in {new_epub_path}")
                new_epub.writestr(file_name, html_content)


if __name__=="__main__":
    # Define the input and output directories
    epub_path = "[WN] ReZero - Volume 37.epub"
    input_directory = 'translation'
    output_directory = 'html'
    # merge(input_directory, output_directory, epub_path)
    html_files = [os.path.join(output_directory, f) for f in os.listdir(output_directory) if f.endswith('.html')+f.endswith('.xhtml')]
    update_epub(epub_path, html_files)