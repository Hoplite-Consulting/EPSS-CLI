#!/bin/bash

echo "Running Startup Script"

# Python Shits
pipreqs --force
pip3 install -r requirements.txt
# rm /workspaces/EPSS-API/requirements.txt

echo "Startup Script Complete"