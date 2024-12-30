import os, json

from getID import getNthCombination


# add the new datas
os.makedirs("new", exist_ok=True)
files = os.listdir("new")
currentLength = len(os.listdir("profiles"))
persons = []

index = -1

for index, file in enumerate(files):
    with open(f"new/{file}", "rb") as f:
        data = json.load(f)

    id = getNthCombination(currentLength + index)
    age = data["age"]
    dob = data["dob"]
    bn = data["bn"]
    en = data["en"]
    date = data["date"]
    newData = {
        "id": id,
        "age": age,
        "dob": dob,
        "bn": bn,
        "en": en,
    }
    searchable = {
        "id": id,
        "name": {"bn": bn["name"], "en": en["name"]},
        "profession": {"bn": bn["profession"], "en": en["profession"]},
        "info": {"bn": bn["info"], "en": en["info"]},
        "date": date,
        "hasImage": 0,
    }
    persons.append(searchable)

    with open(f"profiles/{id}.json", "w", encoding="utf8") as f:
        json.dump(newData, f, ensure_ascii=False)

    try:
        os.remove(f"new/{file}")
        print(f"Removed new/{file}")
    except Exception as e:
        print(f"Failed to remove new/{file}: {e}")


print(f"Current Profiles:", currentLength + index + 1)

with open("searchableData.json", "rb") as f:
    data = json.load(f)

data.extend(persons)

with open("searchableData.json", "w", encoding="utf8") as f:
    json.dump(data, f, ensure_ascii=False)
