#!/bin/bash

# Navigate to the script's directory
cd "$(dirname "$0")"

# Run the update script
python3 update_hosts.py

# Git operations
git add .
git commit -m "Update hosts: $(date '+%Y-%m-%d %H:%M:%S')"

# Push to main
git push -u origin main
