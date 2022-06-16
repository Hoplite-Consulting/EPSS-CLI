#!/bin/python3

from src import *
import sys
from alive_progress import alive_bar
import csv

if __name__ == "__main__":
    eps = epss()

    try:
        readFile = sys.argv[1]
    except IndexError:
        print("CVS File not included: ./epss.py <path_to_input_file>")
        exit(1)
    try:
        writeFile = sys.argv[2]
    except IndexError:
        writeFile = sys.argv[1].split(".")[0]+"_out.csv"

    with open(readFile, "r") as read, open(writeFile, "w", newline='') as write:
        reader = csv.DictReader(read)
        fields = reader.fieldnames
        fields.append(cveData.epss)
        fields.append(cveData.percentile)
        writer = csv.DictWriter(write, fields)
        writer.writeheader()
        with alive_bar(len(list(reader))) as bar:
            for row in reader:
                cve = row["CVE"]
                resp = eps.get(cve)
                row[resp.epss] = resp.EPSS
                row[resp.percentile] = resp.PERCENTILE
                writer.writerow(row)
                bar()