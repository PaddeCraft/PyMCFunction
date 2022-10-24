import os
import json
import shutil
import hashlib
import requests
from zipfile import ZipFile

hashes = []
basePath = "pymcfunction/update_specific_types/"
newReleaseRequired = False


def hash(pth):
    md5 = hashlib.md5()
    with open(pth, "rb") as fl:
        while True:
            data = fl.read(65536)
            if not data:
                break
        md5.update(data)


for f in ["advancement.py", "block.py", "entity.py", "item.py", "effect.py"]:
    hashes.append(hash(basePath + f))

print("Getting metadata...")

launchermeta = requests.get(
    "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
).json()

latestVersion = launchermeta["latest"]["release"]

for v in launchermeta["versions"]:
    if v["id"] == latestVersion:
        version = v
        break

versionmeta = requests.get(v["url"]).json()
clientUrl = versionmeta["downloads"]["client"]["url"]

print("Getting client file...")

with open("client.jar", "wb") as c:
    c.write(requests.get(clientUrl).content)

print("Reading client file...")

with ZipFile("client.jar", "r") as zipObj:
    zipObj.extract("assets/minecraft/lang/en_us.json", path=".")

with open("assets/minecraft/lang/en_us.json", "r", encoding="UTF-8") as f:
    content = json.load(f)

print("Removing unnessecary files...")

shutil.rmtree("assets")
os.remove("client.jar")

advancements = []
entities = []
effects = []
blocks = []
items = []

print("Parsing language file...")

for id in content:
    try:
        if id[0:5] == "block":
            part = id.split(".", maxsplit=2)[2]
            if len(part.split(".")) == 1:
                blocks.append("    " + part.upper() + ' = "minecraft:' + part + '"')
        if id[0:4] == "item":
            part = id.split(".", maxsplit=2)[2]
            if len(part.split(".")) == 1:
                items.append("    " + part.upper() + ' = "minecraft:' + part + '"')
        if id[0:6] == "entity":
            part = id.split(".", maxsplit=2)[2]
            if len(part.split(".")) == 1:
                entities.append("    " + part.upper() + ' = "minecraft:' + part + '"')
        if id[0:6] == "effect":
            part = id.split(".", maxsplit=2)[2]
            if len(part.split(".")) == 1:
                effects.append("    " + part.upper() + ' = "minecraft:' + part + '"')
        if id[0:12] == "advancements":
            parts = id.split(".")
            if parts[-1] == "title":
                advancements.append(
                    "    "
                    + "_".join(parts[1:-1])
                    + ' = "'
                    + parts[1]
                    + "/"
                    + "_".join(parts[2:-1])
                    + '"'
                )
    except IndexError:
        pass

print("Generate and write files...")

advancementStr = "from enum import Enum\n\n\nclass Advancement(Enum):\n"
advancementStr += "\n".join(advancements) + "\n"
entityStr = "from enum import Enum\n\n\nclass Entity(Enum):\n"
entityStr += "\n".join(entities) + "\n"
effectStr = "from enum import Enum\n\n\nclass Effect(Enum):\n"
effectStr += "\n".join(effects) + "\n"
blockStr = "from enum import Enum\n\n\nclass Block(Enum):\n"
blockStr += "\n".join(blocks) + "\n"
itemStr = "from enum import Enum\n\n\nclass Item(Enum):\n"
itemStr += "\n".join(items) + "\n"

with open(basePath + "advancement.py", "w+", encoding="UTF-8") as f:
    f.write(advancementStr)

with open(basePath + "entity.py", "w+", encoding="UTF-8") as f:
    f.write(entityStr)

with open(basePath + "effect.py", "w+", encoding="UTF-8") as f:
    f.write(effectStr)

with open(basePath + "block.py", "w+", encoding="UTF-8") as f:
    f.write(blockStr)

with open(basePath + "item.py", "w+", encoding="UTF-8") as f:
    f.write(itemStr)

for f in ["advancement.py", "block.py", "entity.py", "item.py", "effect.py"]:
    if not hash(basePath + f) in hashes:
        newReleaseRequired = True

print("Done.")

print("::set-output name=release::" + ("true" if newReleaseRequired else "false"))
