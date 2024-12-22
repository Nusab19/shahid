import os, json


with open("searchableData.json", "rb") as f:
    data = json.load(f)

with open("rawData.json", "rb") as f:
    rawData = json.load(f)


def sanitizeText(text, lang="en"):
    text = " ".join(text.split())
    text = text.replace("\n", ", ").strip()

    if text and not text.endswith((".", "।")):
        text += "." if lang == "en" else "।"
    
    return (text[0] + text[1:]) if text else text


def pprint(text):
    print(json.dumps(text, indent=2, ensure_ascii=False))


def cleanup(data, lang="en"):
    name = data["name"]
    born = data["bornDate"]
    birthPlace = data["bornAddress"]
    profession = data["educationOrWork"]
    bio = data["biography"]
    cause = data["howToDeath"]
    shortCause = cause["short"]
    longCause = cause["long"]
    return {
        "name": sanitizeText(name, lang),
        "born": sanitizeText(born, lang),
        "birthPlace": sanitizeText(birthPlace, lang),
        "profession": sanitizeText(profession, lang),
        "bio": sanitizeText(bio, lang),
        "cause": {
            "short": sanitizeText(shortCause, lang),
            "long": sanitizeText(longCause, lang),
        },
    }


os.makedirs("profiles", exist_ok=True)

for i in range(len(rawData)):
    id = data[i]["id"]
    raw = rawData[i]
    age = raw.get("age", "").strip()
    bn = cleanup(rawData[i]["bn"], "bn")
    en = cleanup(rawData[i]["en"], "en")
    newData = {
        "id": id,
        "age": age,
        "bn": bn,
        "en": en,
    }
    with open(f"profiles/{id}.json", "w", encoding="utf8") as f:
        json.dump(newData, f, ensure_ascii=False)

    print(f"{i:03}. {id}")
