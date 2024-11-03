# Usage
To translate any epub book with this repository:
1) Download .py files in repository, place epub file and py files in the same directory
2) Change variable epub_path to epub's name in file '1 - split_epub.py', line 51 and run it
3) Run file '2 - create_request.py'. You can change translation laguages on line 32. Change prompt according to your needs
4) Create environment variable OPENAI_API_KEY with value of your openai's key (300 pages cost apr. 10 cents)
   OR
   Upload your jsonl file to ChatGPT UI
5) Wait until batch complition
6) Retreave batch result with it's file-id
   OR
   Download it from UI
7) Define the input file in "5 - batch_to_txt.py", run it
8) Merge files to html using '6 - merge.py'
9) Replace html files in epub using Sigil, for example. Probably it's possible to use python for that.
