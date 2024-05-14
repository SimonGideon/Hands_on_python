#!/bin/bash

# Base directory
BASE_DIR="/home/simon/Documents/extras/Hands_on_python/forex-sampling"
DOWNLOAD_DIR="/home/simon/Downloads"

# Activate the virtual environment
source $BASE_DIR/venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install pandas openpyxl pdfkit

# Check if wkhtmltopdf is installed, if not, install it
if ! command -v wkhtmltopdf &> /dev/null; then
    echo "wkhtmltopdf is not installed. Installing now..."
    sudo apt-get update
    sudo apt-get install -y wkhtmltopdf
else
    echo "wkhtmltopdf is already installed."
fi

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
