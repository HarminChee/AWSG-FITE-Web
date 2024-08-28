#!/bin/bash

# Navigate to the directory where app.py is located
cd "$(dirname "$0")"

# Start the Flask app in the background
python3 app.py &

# Open the index.html (or fite.html) file in the default web browser
open index.html  # For macOS
# start index.html  # For Windows
# xdg-open index.html  # For Linux
