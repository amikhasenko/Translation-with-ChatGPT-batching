# About

This repository was created to translate the Re:Zero web novel into German, aiming to make the translation process cost-effective and repeatable. Current options of translating:
1. Do not support EPUB translations.
2. Do not utilize AI translation, what limits quality.
3. Expensive.

# Cost Overview

As of November 3, 2024:

Translating approximately 300 pages costs around 7 cents.

The minimum deposit amount for ChatGPT is 5 euros, plus a commission fee.

Please note that the ChatGPT deposit expires one year after the transfer.

# Usage Instructions

To translate any EPUB book using this repository:

1. Clone repository and install dependances (using python 3.12+)
```
git clone 
```
3. Set up an environment variable named `OPENAI_API_KEY` with your OpenAI API key and execute the `3 - create_batch.py` file

   Alternatively,

   Upload your JSONL file to the ChatGPT UI.
5. Wait for the batch processing to complete.
6. Retrieve the batch result using its file ID.

   Alternatively,

   Download it directly from the UI.
7. Specify the input file in `5 - batch_to_txt.py` and run it.
8. Merge the files into HTML format using `6 - merge.py`.
9. Replace the HTML files in the EPUB using a tool like Sigil. It's also possible to automate this process with Python.

# To do list
- [X] organise code 
- [X] create config file
- [X] create CLI (`main.py`)
- [ ] create `requirements.txt` file
- [ ] create UI
- [ ] test on different machines
- [ ] make a release 
