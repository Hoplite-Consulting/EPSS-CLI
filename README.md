# EPSS API

EPSS API is an asynchronos python script that utilizes First.org's EPSS API to parse through CVE's and return the EPSS score and percentile appended to the last columns of a CSV file.  This was tested utilizing CSV output from Tenable IO and Nessus Professional.  

Written by Oliver Scotten.

### Requirements
- Python 3.10.4 or greater

### Use Instructions
- Install requirements
```
pip3 install -r requirements.txt
```

### Run
```
./epss.py --help
OR
./epss.py <read_file>
```
