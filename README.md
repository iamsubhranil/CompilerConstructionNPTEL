Complete pipeline to generate transcriptions, summaries and subtitles for 
![ACM 2019 Summer School of Compiler Construction](https://archive.nptel.ac.in/courses/128/106/128106009/) course by NPTEL.

```
$ mkdir audios subtitles segments transcripts
$ pip install -r requirements.txt
$ python 01_extract_links.py
$ echo '{"username": "<huggingfaceusername>", "password": "<huggingfacepassword>"}' > .env
$ python 02_summarize.py
$ python 03_generate_subtitles.py
```
