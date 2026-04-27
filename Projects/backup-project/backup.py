import os
import shutil
from datetime import datetime

source_folder = "source"
backup_root = "backups"

# Create timestamp folder
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_folder = os.path.join(backup_root, f"backup_{timestamp}")

os.makedirs(backup_folder, exist_ok=True)

# Copy files
for file_name in os.listdir(source_folder):
    source_file = os.path.join(source_folder, file_name)

    if os.path.isfile(source_file):
        shutil.copy2(source_file, backup_folder)
        print(f"Backed up: {file_name}")

print(f"\nBackup completed at: {backup_folder}")