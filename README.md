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

1. Set up an environment variable named `OPENAI_API_KEY` with your OpenAI API key
2. Clone repository and install dependances (using python 3.11+ - tested on python 3.12.3)
```
git clone https://github.com/amikhasenko/Translation-with-ChatGPT-batching.git
cd Translation-with-ChatGPT-batching
pip install -r requirements.txt
```
3. Edit `config.toml`
4. Launch main script
```
python3 main.py
```
5. Wait for the batch to complete and launch main script again. If the batch is completed it will replace epub file with it's translated version, if not - it'll show status and starting time.

# To do list
- [X] organise code 
- [X] create config file
- [X] create CLI (`main.py`)
- [X] create `requirements.txt` file
- [ ] create UI
- [ ] test on different machines
- [ ] make a release 
