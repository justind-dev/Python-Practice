from pathlib import Path
from time import ctime
import shutil
# Location of file (this is going to look in the relative directory to this script, put you can specify
# /home/user/desktop or c:\users\username\desktop\ etc... when needed)
path = Path("test_file.txt")

# Check whether it exists
print(path.exists())

# Set a new file name variable
new_name = "test_file_new_name.txt"

# rename to the variable above
path.rename(new_name)

#reset the path variable to point to the new name
path = Path(new_name)

# print creation time in user friendly format
print(f"Created: {ctime(path.stat().st_ctime)}")

# Be aware that the following write operations OVERWRITE files, does not append.
path.write_text("THIS IS A NEW LINE OF TEXT")

# Meaning, the file will only contain this line after the program runs
path.write_text("THIS IS ANOTHER LINE OF TEXT")

print(path.read_text())

# Copying files using shutil
source = path
target = Path("other_file.txt")
shutil.copy(source,target)