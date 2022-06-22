# Python EPSS API

EPSS API is an asynchronos python script that utilizes First.org's EPSS API to parse through CVE's and return the EPSS score and percentile appended to the last columns of a CSV file.  This was tested utilizing CSV output from Tenable.io and Nessus Professional.

The epss.py script will read a CSV file, Identify the CVE's within, and append the corresponding EPSS score and percentile to the last columns in the CSV file.

The cve-epss.py script is a standalone python-based API that will retrieve the EPSS and percentile for a given CVE.  This can also handle multiple CVE's as well as dates for EPSS scores and percentiles at a given point in time.  

Written by [Oliver Scotten](https://www.github.com/oliv10).

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

### Manual CVE Lookup
Space separated for multiple CVE lookup.
```
./cve_epss.py --help
OR
./cve_epss.py <cve-20xx-xxxx> <cve-20xx-xxxx>
```

### Manual CVE & Date Lookup
```
./cve-epss.py <cve-2022-xxxx> --date <yyyy-mm-dd>
```
