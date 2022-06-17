#!/bin/python3

from src import *
import os.path as p
from alive_progress import alive_bar
import csv
import argparse

if __name__ == "__main__":

    # Args 
    parser = argparse.ArgumentParser(description="./epss.py <read_file>")
    parser.add_argument('readFile', help="Read File Location")
    parser.add_argument('-w', '--writeFile', metavar="", help="Write File Location")
    parser.add_argument('-v', '--verbose', action='store_true', help="Verbose Output")
    args = parser.parse_args()

    # Set Read / Write Files
    readFile = args.readFile
    if args.writeFile == None:
        writeFile = readFile.split(".")[0]+"_out.csv"
    else:
        writeFile = args.writeFile
    
    # Check if Write File Exists / Ask to overwrite...
    if (p.exists(writeFile)):
            while True:
                rm = input("Do you want to overwrite '" + writeFile + "'? [yes/no]: ")
                if rm.lower() == "no":
                    print("Terminating...")
                    exit()
                elif rm.lower() == "yes":
                    break

    eps = epss(args.verbose)

    # Strange work around to count number of rows in csv file to not cause a crash.
    # Causes crash whe using len(list(reader)). Unkown as to why...
    def getRows(file):
        rows = 0
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows += 1
        return rows

    with open(readFile, "r") as read, open(writeFile, "w", newline='') as write:
        reader = csv.DictReader(read)
        fields = reader.fieldnames
        fields.append(cveData.epss)
        fields.append(cveData.percentile)
        writer = csv.DictWriter(write, fields)
        writer.writeheader()
        with alive_bar(getRows(readFile)) as bar:
            for row in reader:
                cve = row["CVE"]
                resp = eps.get(cve)
                row[resp.epss] = resp.EPSS
                row[resp.percentile] = resp.PERCENTILE
                writer.writerow(row)
                bar()