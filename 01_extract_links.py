import requests
import re
import whisper
from pytube import YouTube

URL="https://archive.nptel.ac.in/courses/128/106/128106009/"

page = requests.get(URL).content.decode("utf-8")

videos = re.findall("change_video_path\(.*\)\";[\s]*\>[a-zA-Z0-9-\s–]*", page)

links = {}

MODELNAME = "medium"
print("Loading whisper model", MODELNAME, "..")
model = whisper.load_model(MODELNAME)

for video in videos:
    link = video.replace("change_video_path(", "")\
        .replace("\n", "").replace("\t","")\
        .replace("–", "-").split(",")[1]\
        .replace(")\"; ","").replace("'", "")
    link = link.split(">")
    links[link[1]] = link[0]
    print("Downloading", link[1])
    yt = YouTube("https://youtube.com/watch?v=" + link[0])
    audio = yt.streams.filter(only_audio=True).first()
    audio.download("audios/" + audio.default_filename)
    print("Transcribing", link[1])
    result = model.transcribe("audios/" + audio.default_filename)
    print(result["text"])
    with open("transcripts/" + audio.default_filename.replace(".mp4", ".txt"), "w") as f:
        f.write(result["text"])
    with open("segments/" + audio.default_filename.replace(".mp4", ".segments"), "w") as f:
        f.write(str(result["segments"]))
