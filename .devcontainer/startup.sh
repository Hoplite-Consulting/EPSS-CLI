#!/bin/bash

echo "Running Startup Script"

# Python Shits
pipreqs /workspaces/EPSS-API/ --force
pip3 install -r /workspaces/EPSS-API/requirements.txt
# rm /workspaces/EPSS-API/requirements.txt

echo "Startup Script Complete"