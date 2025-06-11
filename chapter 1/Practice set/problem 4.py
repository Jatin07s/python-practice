import os

# select the directory whose contents you want to List
directory_path = '.'

# Select the entries you anna put that
entries = os.listdir(directory_path)

# Create the entry you want to generate
for entry in entries:
    print(entry)
