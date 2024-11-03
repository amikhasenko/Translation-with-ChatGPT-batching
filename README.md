# About

This repository was created to translate the Re:Zero web novel into German, aiming to make the translation process cost-effective and reproducible. Current alternatives on GitHub often:
1. Do not support EPUB translations.
2. Do not utilize ChatGPT, leading to subpar results.
3. Do not implement batching, which makes translations twice as expensive.

# Cost Overview

As of November 3, 2024:

Translating approximately 300 pages costs around 7 cents.

The minimum deposit amount for ChatGPT is 5 euros, plus a commission fee.

Please note that the ChatGPT deposit expires one year after the transfer.

# Usage Instructions

To translate any EPUB book using this repository:

1. Download the `.py` files from the repository and place both the EPUB file and the Python files in the same directory.
2. Modify the `epub_path` variable in the `1 - split_epub.py` file (line 51) to match the name of your EPUB file, then run the script.
3. Execute the `2 - create_request.py` file. You can adjust the translation languages on line 32 and modify the prompt to suit your needs.
4. Set up an environment variable named `OPENAI_API_KEY` with your OpenAI API key and execute the `3 - create_batch.py` file

   Alternatively,

   Upload your JSONL file to the ChatGPT UI.
5. Wait for the batch processing to complete.
6. Retrieve the batch result using its file ID.

   Alternatively,

   Download it directly from the UI.
7. Specify the input file in `5 - batch_to_txt.py` and run it.
8. Merge the files into HTML format using `6 - merge.py`.
9. Replace the HTML files in the EPUB using a tool like Sigil. It's also possible to automate this process with Python.
