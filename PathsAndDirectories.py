from pathlib import Path

# Set you path
path = Path("c:/1/")

# Path comprehension to find directories
directories = [d for d in path.iterdir() if d.is_dir()]

# Path comprehension to find files of a certain type
files = [g for g in path.glob("*.txt")]

# Path comprehension to find files of a certain type, recursively
files = [g for g in path.rglob("*.txt")]


print(directories)

print(files)
