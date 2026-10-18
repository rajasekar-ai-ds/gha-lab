import json
import os


data = {"weight" : 0.42, "version" : 1}
with open("model.json", "w") as file:
	json.dump(data, file)

print("model.json is saved")

try:
	path = os.environ["GITHUB_OUTPUT"]
except KeyError:
	print("GITHUB_OUTPUT not set (local run) - skipping output")
else:
	with open(path, 'a') as f:
		f.write(f"version={data['version']}\n")

print("Small change 2")



