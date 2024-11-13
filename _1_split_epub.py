import os
import zipfile
from bs4 import BeautifulSoup

# Function to split HTML content into chunks of no more than 50,000 characters based on paragraphs
# 50_000/4 = 12_500 - approximate amonnt of tockens, works for englich-like languges
def split_html_into_chunks(html_content: str, max_chars: int = 50_000, delimator: str = "\n") -> list[str]:
    """
    Splits HTML or text content into manageable chunks based on a specified character limit and delimiter.

    This function divides a large HTML or text file into smaller chunks, with each chunk containing
    no more than `max_chars` characters. By default, it splits content based on paragraphs (using a newline as the
    delimiter). For sentence-based splitting, use `delimator = "."`.

    Parameters:
    ----------
    html_content : str
        The HTML or text content to split into chunks.
    max_chars : int, optional
        The maximum number of characters allowed in each chunk (default is 50,000 characters).
    delimator : str, optional
        The character or string to split the content on. Defaults to `\n` for paragraph splitting.
        Use `"."` for sentence splitting, or specify any other delimiter as needed.

    Returns:
    -------
    list[str]
        A list of strings, where each string is a chunk of the original content
        that does not exceed the `max_chars` limit.

    Example:
    -------
    >>> html_content = "<p>This is a paragraph.</p><p>This is another paragraph.</p>"
    >>> chunks = split_html_into_chunks(html_content, max_chars=50, delimator="\n")
    >>> for chunk in chunks:
    >>>     print(chunk)

    Notes:
    ------
    - If the content is split based on sentences, set `delimator` to `"."`.
    - Each chunk will include only complete paragraphs or sentences, up to the character limit.
    """

    paragraphs = html_content.split(delimator)
    chunks, current_chunk = [], ""
    for paragraph in paragraphs:
        # Add paragraph if it fits within the limit
        if len(current_chunk) + len(paragraph) + 1 <= max_chars:  # +1 for '\n' separator
            current_chunk += paragraph + '\n'
        else:
            # Save current chunk and start a new one
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + '\n'
    if current_chunk:
        chunks.append(current_chunk.strip())  # Add any remaining text as the last chunk
    return chunks


def extract_epub_content(epub_path):
    """
    Extracts the main HTML content from an EPUB file for translation or text processing.

    This function opens an EPUB file (which is essentially a ZIP archive) and extracts the
    content of files with `.html` or `.xhtml` extensions, which typically contain the
    primary readable content. The HTML content from each file is parsed and stored in
    a dictionary with file names as keys.

    Parameters:
    ----------
    epub_path : str
        Path to the EPUB file.

    Returns:
    -------
    dict
        A dictionary where keys are file names of HTML/XHTML files within the EPUB,
        and values are strings containing the parsed HTML content of each file.

    Example:
    -------
    >>> content = extract_epub_content("example.epub")
    >>> for file_name, html_content in content.items():
    >>>     print(f"File: {file_name}")
    >>>     print(html_content)
    """
    content_html = {}
    
    with zipfile.ZipFile(epub_path, 'r') as epub_zip:
        for file_name in epub_zip.namelist():
            # EPUB content is usually found in files with .xhtml or .html extensions
            if file_name.endswith(('.xhtml', '.html')):
                with epub_zip.open(file_name) as file:
                    soup = BeautifulSoup(file.read(), 'html.parser')
                    html_content = str(soup)
                    content_html[file_name] = html_content
    
    return content_html

# Step 1: Split EPUB into smaller text files and save with references to HTML files
def split_epub(epub_path, output_folder):
    """
    Splits the content of an EPUB file into manageable text chunks and saves them to a specified folder.

    This function extracts HTML content from the provided EPUB file, divides the content of each HTML/XHTML
    file into smaller chunks, and saves each chunk as a separate text file in the specified output folder.
    Each output file includes a header indicating the original HTML source file name.

    Parameters:
    ----------
    epub_path : str
        Path to the EPUB file to process.
    output_folder : str
        Path to the folder where the split text files will be saved. This folder will be created if it doesn't exist.

    Returns:
    -------
    None
        The function saves the split chunks as text files in the specified folder but does not return any value.

    File Format:
    -----------
    Each output file is named in the format `request-{chunk_counter}.txt`, where `chunk_counter` is an incremented
    counter for each chunk created across all HTML files. The beginning of each file contains a comment header
    (`<!-- Source: {file_name} -->`) that indicates the original HTML file the chunk was extracted from.

    Example:
    -------
    >>> split_epub("example.epub", "output_folder")
    # This will create a series of text files in `output_folder`, each containing a chunk of text from the EPUB.

    Dependencies:
    ------------
    - Requires `extract_epub_content` to extract HTML content from the EPUB file.
    - Uses `split_html_into_chunks` to split the HTML content into manageable pieces.

    Notes:
    ------
    - The `split_html_into_chunks` function's default chunk size is 50,000 characters.
    - Ensure `output_folder` has the appropriate write permissions if it's an existing directory.
    """

    os.makedirs(output_folder, exist_ok=True)
    content_html = extract_epub_content(epub_path)
    chunk_counter = 0

    for file_name, html_content in content_html.items():
        chunks = split_html_into_chunks(html_content)
        for chunk in chunks:
            with open(os.path.join(output_folder, f"request-{chunk_counter}.txt"), 'w', encoding='utf-8') as file:
                # Add header to indicate the original HTML file
                file.write(f"<!-- Source: {file_name} -->\n")
                file.write(chunk)
            chunk_counter += 1

# Usage
if __name__=="__main__":
    epub_path = "[WN] ReZero - Volume 38.epub"
    output_folder = "output_requests"
    split_epub(epub_path, output_folder)

