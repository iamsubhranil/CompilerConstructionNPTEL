from hugchat import hugchat
from hugchat.login import Login
import json
import glob
# Log in to huggingface and grant authorization to huggingchat
auth = {}
print("Logging to HuggingFace..")
with open(".env", "r") as f:
    auth = json.loads("\n".join(f.readlines()))
sign = Login(auth["username"], auth["password"])
cookies = sign.login()

# Save cookies to the local directory
cookie_path_dir = "./cookies_snapshot"
sign.saveCookiesToDir(cookie_path_dir)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

files = glob.glob("transcripts/*.txt")

for file in files:
    if file == "requirements.txt" or file.endswith(" - Summary.txt"):
        continue
    print("\nGenerating summary for", file, "..")
    with open(file, "r") as f:
        lecture = "\n".join(f.readlines())
        resp = chatbot.query("Create exam notes from the following lecture, explaining the technical terms mentioned:\n" + lecture)
        summary_file = file.replace(".txt", " - Summary.txt").replace("transcripts", "summaries")
        with open(summary_file, "w") as f2:
            print(resp["text"])
            f2.write(resp["text"])
