import os
import subprocess

# Change to the current directory
os.chdir('.')

# Get a list of all files in the current directory
files = os.listdir()

# Git add and commit each file
for file in files:
    if os.path.isfile(file):
        # Git add
        subprocess.run(['git', 'add', file])

        # Git commit with the filename as the commit message
        subprocess.run(['git', 'commit', '-m', file])

# Git push
subprocess.run(['git', 'push'])
