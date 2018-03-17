# small example of using json package
import json
data = {'film1': 9.2, 'film2': 8.9, 'film3': 8.2}
file = open("test.json", "w", encoding="utf-8")
json.dump(data, file)
file = open("test.json", "r", encoding="utf-8")
data = json.loads(file.read())
print(data)
file.close()



