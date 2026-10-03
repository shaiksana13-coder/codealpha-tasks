import os
import shutil

source_folder = "images"
destination_folder = "jpg_files"

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source = os.path.join(source_folder, filename)
        destination = os.path.join(destination_folder, filename)

        shutil.move(source, destination)
        print(filename, "moved successfully")

print("Task completed!")