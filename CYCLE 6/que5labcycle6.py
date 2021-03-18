f = open("New.csv", "a")
import json

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("New.csv", "r")
print(f.read())