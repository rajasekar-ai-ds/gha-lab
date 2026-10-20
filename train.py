import json
import os
import platform


data = {"weight" : 0.42, "version" : 1, "python" : platform.python_version()}
with open("model.json", "w") as file:
	json.dump(data, file)

print("model.json is saved")

try:
	path = os.environ["GITHUB_OUTPUT"]
except KeyError:
	print("GITHUB_OUTPUT not set (local run) - skipping output")
else:
	with open(path, 'a') as f:
		f.write(f"version={data['version']}-{data['python']}\n")


epochs = int(os.environ.get('EPOCHS') or "5")

print(f"Train for {epochs} epochs")