import os

# Specify the target directory
directory = 'D:\Games\Emulation\RetroAchievements\SaveStates\House\minigame states'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Full path to the original file
    original_file = os.path.join(directory, filename)
    
    # Skip if it's not a file
    if not os.path.isfile(original_file):
        continue

    # Split the filename and extension
    name, ext = os.path.splitext(filename)
    
    # Skip if the filename is less than 4 characters
    if len(name) < 4:
        continue

    # Extract the last four letters and construct the new filename
    last_four = name[-2:]
    new_name = last_four + " - " + name[:-7] + ext
    
    if name[-2:] != "- ":
    # Full path to the new file
    new_file = os.path.join(directory, new_name)
    
    # Rename the file
    os.rename(original_file, new_file)
    print(f'Renamed: {filename} -> {new_name}')