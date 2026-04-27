# Backup Script

## Overview
This project automates file backups by copying files from a source folder into a timestamped backup directory.

---

## Features
- Copies files from source folder  
- Creates timestamped backup folders  
- Prevents overwriting previous backups  
- Simple automation using Python  

---

## How It Works
The script reads all files in the source folder and copies them into a new backup directory labeled with the current timestamp.

---

## How to Run
python backup.py

---

## Example Output
Backed up: sample.txt  
Backup completed at: backups/backup_2026-04-20_21-57-50

---

## Future Improvements
- Add file compression 
- Allow user-defined source folder  
- Schedule automatic backups  
