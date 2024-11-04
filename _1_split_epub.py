import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Function to split HTML content into chunks of no more than 60,000 characters based on paragraphs
def split_html_into_chunks(html_content, max_chars=50000):
    paragraphs = html_content.split('\n')
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

# Function to extract HTML content from HTML files in the EPUB
def extract_epub_content(epub_path):
    book = epub.read_epub(epub_path)
    content_html = {}

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            html_content = str(soup)
            content_html[item.file_name] = html_content
    
    return content_html

# Step 1: Split EPUB into smaller text files and save with references to HTML files
def split_epub(epub_path, output_folder):
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

