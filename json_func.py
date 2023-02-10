import json

def open_json(filename):
	with open(filename) as file:
		return json.load(file)

def save_json(data, filename):
	print(data)
	with open(filename, "w") as file:
		json.dump(data, file, indent=4)


a = open_json("items.json")

save_json(a, "items.json")