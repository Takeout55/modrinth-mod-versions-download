import requests
import os

def download(url, path, chunk_size=64 * 1024):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)


ID = input("Enter the Mod ID")
modname = input("Enter the Mod Name")

url = f"https://api.modrinth.com/v2/project/{ID}/version?"

resp = requests.get(url=url)
data = resp.json()

name  = [v["name"] for v in data]
urls  = [
    f["url"]
    for v in data
    for f in v["files"]
]

x = 0
for i in urls:
    print(urls[x])
    if os.path.isdir(f"./mods/{modname}"):
        download(urls[x], f"./mods/{modname}/{name[x]}")
    else:
        os.makedirs(f"./mods/{modname}")
        download(urls[x], f"./mods/{modname}/{name[x]}")
    x = x + 1

