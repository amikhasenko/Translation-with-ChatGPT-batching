# About

Repository was used to translate Re:Zero web novel on German, with attempt to make translation cheap and reproducible. 
Alternative options on github either
1) don't support epub translations
2) don't use ChatGPT, what causes poor results
3) don't use batching, what makes translation 2 times more expencive

# How expensive is it?

Currently (03.11.2024):

300 pages cost apr. 7 cents

Minimal deposit amount to ChatGPT is 5 euro + commission 

ChatGPT deposit expires a year after transfer

# Usage

To translate any epub book with this repository:
1) Download .py files in repository, place epub file and py files in the same directory
2) Change variable epub_path to epub's name in file '1 - split_epub.py', line 51 and run it
3) Run file '2 - create_request.py'. You can change translation laguages on line 32. Change prompt according to your needs
4) Create environment variable OPENAI_API_KEY with value of your openai's key
   
   OR
   
   Upload your jsonl file to ChatGPT UI
6) Wait until batch complition
7) Retreave batch result with it's file-id
   
   OR
   
   Download it from UI
9) Define the input file in "5 - batch_to_txt.py", run it
10) Merge files to html using '6 - merge.py'
11) Replace html files in epub using Sigil, for example. Probably it's possible to use python for that.
