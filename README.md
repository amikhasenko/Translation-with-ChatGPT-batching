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
2. Clone repository and install dependances (using python 3.12+)
```
git clone https://github.com/amikhasenko/Translation-with-ChatGPT-batching.git
pip install -r requirements.txt
cd Translation-with-ChatGPT-batching
```
3. Edit `config.toml`
4. Launch main script
```
python3 main.py
```

# To do list
- [X] organise code 
- [X] create config file
- [X] create CLI (`main.py`)
- [ ] create `requirements.txt` file
- [ ] create UI
- [ ] test on different machines
- [ ] make a release 
