#!/bin/bash

# Base directory
BASE_DIR="/home/simon/Documents/extras/Hands_on_python/forex-sampling"

# Activate the virtual environment
source $BASE_DIR/forexSampling/bin/activate

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt..."
pip install -r $BASE_DIR/requirements.txt

# Check if wkhtmltopdf is installed, if not, install it
if ! command -v wkhtmltopdf &> /dev/null; then
    echo "wkhtmltopdf is not installed. Installing now..."
    sudo apt-get update
    sudo apt-get install -y wkhtmltopdf
else
    echo "wkhtmltopdf is already installed."
fi
