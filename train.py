import json
import os


data = {"weight" : 0.42, "version" : 1}
with open("model.json", "w") as file:
	json.dump(data, file)

print("model.json is saved")

try:
	v = os.environ["GITHUB_OUTPUT"]
	file2 = open(v, 'a')
except KeyError:
	print("ENV not found, Check your environment")
else:
	file2.write(f"version={data['version']}\n")
	file2.close()





