#!/bin/bash

# Base directory
BASE_DIR="/home/simon/Documents/extras/Hands_on_python/forex-sampling"
DOWNLOAD_DIR="/home/simon/Downloads"

# Activate the virtual environment
source $BASE_DIR/venv/bin/activate

# Absolute path to the Python script
PYTHON_SCRIPT="$BASE_DIR/csv_pdf.py"

# Prompt the user to enter the path of the CSV file
read -p "Enter the path of the CSV file: " CSV_NAME

CSV_PATH="$DOWNLOAD_DIR/$CSV_NAME"

echo "CSV file: $CSV_NAME"
# Check if the CSV file exists
if [ ! -f "$CSV_PATH" ]; then
    echo "Error: CSV file not found at $CSV_PATH"
    exit 1
fi

# Run the Python script
echo "Running the Python script..."
python3 $PYTHON_SCRIPT "$CSV_PATH"
