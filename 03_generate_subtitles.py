import glob
import json

def convert_time(tm):
    hours = int(tm // 3600)
    tm = tm % 3600
    min_ = int(tm // 60)
    tm = tm % 60
    sec = int(tm)
    mills = int((tm - sec) * 1000)
    return f"{hours:02d}:{min_:02d}:{sec:02d},{mills:03d}"

segments = glob.glob("segments/*.segments")

for segment in segments:
    print(segment)
    with open(segment, "r") as f:
        file = "\n".join(f.readlines())
        seg = eval(file) # BUDDY!
        with open(segment.replace(".segments", ".srt").replace("segments", "subtitles"), "w") as f:
            for part in seg:
                id_ = part["id"] + 1
                start = convert_time(part["start"])
                end = convert_time(part["end"])
                text = part["text"]
                f.write(str(id_) + "\n")
                f.write(start + " --> " + end + "\n")
                f.write(text.strip() + "\n")
                f.write("\n")
