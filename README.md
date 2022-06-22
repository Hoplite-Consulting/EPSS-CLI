# Python EPSS API

The Python EPSS API is an asynchronos python script that utilizes First.org's EPSS API to parse through CVE's within a CSV and return the EPSS scores and percentiles appended to the last columns of the file.  This was tested utilizing CSV output from Tenable.io and Nessus Professional.

The **epss.py** script will read a CSV file, identify the CVE's within, and append the corresponding EPSS score and percentile to the last columns in the CSV file utilizing the [EPSS API](https://api.first.org/data/v1/epss).

The **cve-epss.py** script is a standalone python script that will retrieve the EPSS and percentile for a given CVE via the [EPSS API](https://api.first.org/data/v1/epss).  This can also handle multiple CVE's as well as dates for EPSS scores and percentiles at a given point in time.  

Written by [Oliver Scotten](https://www.github.com/oliv10).

### Requirements
- Python 3.10.4 or greater

### Usage
- Install requirements
```
pip3 install -r requirements.txt
```

### Reading CSV Files
The script will key on files with the column "CVE" and append the corresponding EPSS and percentile to the last two columns within the CSV file.
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
