import json

json_data = []

with open("data/startups_demo.json") as fd:
    for line in fd:
        obj = json.loads(line)
        json_data.append(obj)
        
cities = set()

for obj in json_data:
    cities.add(obj["city"])
    
for city in cities:
    print(f"<option value='{city}'>{city}</option>")