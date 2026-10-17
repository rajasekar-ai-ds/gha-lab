import json 


data = {"weight" : 0.42, "version" : 1}
with open("model.json", "w") as file:
	json.dump(data, file)

print("model.json is saved")

