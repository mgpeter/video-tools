import os

# Directory containing the photos
directory = r'C:\Users\mgpet\OneDrive\Pictures\Photos\2024-06-29-usual-expat-photoshoot'

# Get a list of all files in the directory
files = os.listdir(directory)

# Generate a set of all expected file names
expected_files = {f'2024-06-29 Domography - Usual Expat Appeal - Kingston Upon Thames {i:03d}.jpg' for i in range(1, 1200)}

# Generate a set of all present file names
present_files = set(files)

# Find missing files by subtracting present files from expected files
missing_files = expected_files - present_files

# Output the missing files
if missing_files:
    print("Missing files:")
    for file in sorted(missing_files):
        print(file)
else:
    print("No files are missing.")